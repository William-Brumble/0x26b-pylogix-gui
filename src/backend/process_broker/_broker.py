import zmq
import multiprocessing
from logging import getLogger, NullHandler, DEBUG
from logging.handlers import QueueHandler


class BrokerProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance(
        pywebview_url: str, pylogix_url: str, queue: multiprocessing.Queue
    ):
        if BrokerProcess.__instance is None:
            with BrokerProcess.__lock:
                if BrokerProcess.__instance is None:
                    BrokerProcess.__instance = BrokerProcess(
                        pylogix_url=pylogix_url,
                        pywebview_url=pywebview_url,
                        queue=queue,
                    )
        return BrokerProcess.__instance

    def __init__(
        self, pywebview_url: str, pylogix_url: str, queue: multiprocessing.Queue
    ):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._init,
            kwargs={
                "pywebview_url": pywebview_url,
                "pylogix_url": pylogix_url,
                "queue": queue,
            },
        )

    def start(self):
        self._process.start()

    def join(self):
        self._process.join()

    def is_alive(self):
        return self._process.is_alive()

    def terminate(self):
        return self._process.terminate()

    def _init(
        self,
        pywebview_url: str = "tcp://*:5559",
        pylogix_url: str = "tcp://*:5560",
        queue: multiprocessing.Queue = None,
    ):
        self.logger = getLogger("broker-process")
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(NullHandler())
        if queue:
            self.handler = QueueHandler(queue)
            self.logger.addHandler(self.handler)

        self.context = zmq.Context()
        self.poller = zmq.Poller()
        self.pywebview = self.context.socket(zmq.ROUTER)
        self.pywebview.bind(pywebview_url)
        self.poller.register(self.pywebview, zmq.POLLIN)
        self.pylogix = self.context.socket(zmq.DEALER)
        self.pylogix.bind(pylogix_url)
        self.poller.register(self.pylogix, zmq.POLLIN)

        try:
            self._work()
        except Exception as e:
            self.logger.error(f"broker process encountered an exception: {e}")
        finally:
            self.pywebview.close()
            self.pylogix.close()
            self.context.term()

    def _work(self):
        while True:
            socks = dict(self.poller.poll())

            if socks.get(self.pywebview) == zmq.POLLIN:
                message = self.pywebview.recv_multipart()
                self.pylogix.send_multipart(message)

            if socks.get(self.pylogix) == zmq.POLLIN:
                message = self.pylogix.recv_multipart()
                self.pywebview.send_multipart(message)

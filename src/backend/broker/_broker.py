import zmq
import multiprocessing


class BrokerProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance():
        if BrokerProcess.__instance is None:
            with BrokerProcess.__lock:
                if BrokerProcess.__instance is None:
                    BrokerProcess.__instance = BrokerProcess()
        return BrokerProcess.__instance

    def __init__(self, pywebview_url: str, pylogix_url: str):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._work,
            kwargs={
                "pywebview_url": pywebview_url,
                "pylogix_url": pylogix_url,
            },
        )

    def start(self):
        self._process.start()

    def join(self):
        self._process.join()

    def _init(
        self, pywebview_url: str = "tcp://*:5559", pylogix_url: str = "tcp://*:5560"
    ):
        self.context = zmq.Context()
        self.poller = zmq.Poller()

        self.pywebview = self.context.socket(zmq.ROUTER)
        self.pywebview.bind(pywebview_url)
        self.poller.register(self.pywebview, zmq.POLLIN)

        self.pylogix = self.context.socket(zmq.DEALER)
        self.pylogix.bind(pylogix_url)
        self.poller.register(self.pylogix, zmq.POLLIN)

        self._work()

    def _work(self):
        while True:
            socks = dict(self.poller.poll())

            if socks.get(self.pywebview) == zmq.POLLIN:
                message = self.pywebview.recv_multipart()
                self.pylogix.send_multipart(message)

            if socks.get(self.pylogix) == zmq.POLLIN:
                message = self.pylogix.recv_multipart()
                self.pywebview.send_multipart(message)

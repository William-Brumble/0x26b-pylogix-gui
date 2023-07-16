import zmq
import time
import multiprocessing
from logging import getLogger, NullHandler, DEBUG
from logging.handlers import QueueHandler


class PywebviewProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance(
        pywebview_url: str, queue: multiprocessing.Queue, port: str, token: str
    ):
        if PywebviewProcess.__instance is None:
            with PywebviewProcess.__lock:
                if PywebviewProcess.__instance is None:
                    PywebviewProcess.__instance = PywebviewProcess(
                        pywebview_url=pywebview_url, queue=queue, port=port, token=token
                    )
        return PywebviewProcess.__instance

    def __init__(
        self, pywebview_url: str, queue: multiprocessing.Queue, port: str, token: str
    ):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._init,
            kwargs={
                "pywebview_url": pywebview_url,
                "queue": queue,
                "port": port,
                "token": token,
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

    # everything below this line happens in the new process
    # -------------------------------------------------------------------------

    def _init(
        self,
        pywebview_url: str = "tcp://localhost:5559",
        queue: multiprocessing.Queue = None,
        port: str = "65535",
        token: str = "development_token",
    ):
        self.logger = getLogger("pywebview-process")
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(NullHandler())
        if queue:
            self.handler = QueueHandler(queue)
            self.logger.addHandler(self.handler)

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.connect(pywebview_url)

        try:
            self._work()
        except Exception as e:
            self.logger.error(f"pywebview process encountered exception: {e}")
        finally:
            self.socket.close()
            self.context.term()

    def _work(self):
        while True:
            time.sleep(5)


import zmq
import multiprocessing


class PywebviewProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance():
        if PywebviewProcess.__instance is None:
            with PywebviewProcess.__lock:
                if PywebviewProcess.__instance is None:
                    PywebviewProcess.__instance = PywebviewProcess()
        return PywebviewProcess.__instance

    def __init__(self, pywebview_url: str):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._work,
            kwargs={
                "pywebview_url": pywebview_url,
            },
        )

    def start(self):
        self._process.start()

    def join(self):
        self._process.join()

    def _init(self, pywebview_url: str = "tcp://localhost:5559"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(pywebview_url)

        self._work()

    def _work(self):
        for request in range(1, 120):
            self.socket.send(b"Hello")
            message = self.socket.recv()
            print(f"Received reply {request} [{message}]")

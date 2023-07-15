import zmq
import multiprocessing


class PylogixProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance():
        if PylogixProcess.__instance is None:
            with PylogixProcess.__lock:
                if PylogixProcess.__instance is None:
                    PylogixProcess.__instance = PylogixProcess()
        return PylogixProcess.__instance

    def __init__(self, pylogix_url: str):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._work,
            kwargs={
                "pylogix_url": pylogix_url,
            },
        )

    def start(self):
        self._process.start()

    def join(self):
        self._process.join()

    def _init(self, pylogix_url: str = "tcp://localhost:5560"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.connect(pylogix_url)

        self._work()

    def _work(self):
        while True:
            message = self.socket.recv()
            print(f"Received request: {message}")
            self.socket.send(b"World")

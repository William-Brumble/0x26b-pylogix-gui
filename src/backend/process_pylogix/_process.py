import multiprocessing

from process_pylogix._pylogix import Pylogix


class PylogixProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance(pylogix_url: str, queue: multiprocessing.Queue, simulate: bool):
        if PylogixProcess.__instance is None:
            with PylogixProcess.__lock:
                if PylogixProcess.__instance is None:
                    PylogixProcess.__instance = PylogixProcess(
                        pylogix_url=pylogix_url, queue=queue, simulate=simulate
                    )
        return PylogixProcess.__instance

    def __init__(self, pylogix_url: str, queue: multiprocessing.Queue, simulate: bool):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._init,
            kwargs={"pylogix_url": pylogix_url, "queue": queue, "simulate": simulate},
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
        pylogix_url: str,
        queue: multiprocessing.Queue = None,
        simulate: bool = True,
    ):
        self.pylogix_implementation = Pylogix(
            pylogix_url=pylogix_url, queue=queue, simulate=simulate
        )
        self.pylogix_implementation.work()

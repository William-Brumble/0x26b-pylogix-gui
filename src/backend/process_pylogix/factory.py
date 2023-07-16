from multiprocessing import Queue

from process_pylogix._process import PylogixProcess


class Factory:
    @staticmethod
    def create_pylogix(
        pylogix_url: str = "tcp://localhost:5560",
        queue: Queue = None,
        simulate: bool = True,
    ):
        pylogix = PylogixProcess.get_instance(
            pylogix_url=pylogix_url, queue=queue, simulate=simulate
        )
        return pylogix

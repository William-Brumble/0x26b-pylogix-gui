from multiprocessing import Queue

from process_pywebview._process import PywebviewProcess


class Factory:
    @staticmethod
    def create_pywebview(pywebview_url: str, queue: Queue, port: str, token: str):
        pywebview = PywebviewProcess.get_instance(
            pywebview_url=pywebview_url, queue=queue, port=port, token=token
        )
        return pywebview

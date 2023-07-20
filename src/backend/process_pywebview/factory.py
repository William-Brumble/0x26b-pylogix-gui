from multiprocessing import Queue

from process_pywebview._process import PywebviewProcess


class Factory:
    @staticmethod
    def create_pywebview(
        pywebview_url: str,
        queue: Queue,
        window_name: str,
        port: str,
        token: str,
        debug: bool,
    ):
        pywebview = PywebviewProcess.get_instance(
            pywebview_url=pywebview_url,
            queue=queue,
            window_name=window_name,
            port=port,
            token=token,
            debug=debug,
        )
        return pywebview

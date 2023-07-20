import os
import zmq
import webview
import multiprocessing
from io import StringIO
from contextlib import redirect_stdout
from logging import getLogger, NullHandler, DEBUG
from logging.handlers import QueueHandler

from process_pywebview._app import App
from process_pywebview._server import Server


class PywebviewProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance(
        pywebview_url: str,
        queue: multiprocessing.Queue,
        window_name: str,
        port: str,
        token: str,
        debug: bool,
    ):
        if PywebviewProcess.__instance is None:
            with PywebviewProcess.__lock:
                if PywebviewProcess.__instance is None:
                    PywebviewProcess.__instance = PywebviewProcess(
                        pywebview_url=pywebview_url,
                        queue=queue,
                        window_name=window_name,
                        port=port,
                        token=token,
                        debug=debug,
                    )
        return PywebviewProcess.__instance

    def __init__(
        self,
        pywebview_url: str,
        queue: multiprocessing.Queue,
        window_name: str,
        port: str,
        token: str,
        debug: bool,
    ):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._init,
            kwargs={
                "pywebview_url": pywebview_url,
                "queue": queue,
                "window_name": window_name,
                "port": port,
                "token": token,
                "debug": debug,
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
        window_name: str = "0x26b-pylogix-gui",
        port: str = "65535",
        token: str = "development_token",
        debug: bool = False,
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

        self.application = App(pywebview_url=pywebview_url, queue=queue)

        self.gui_dir = os.path.join(os.path.dirname(__file__), "dist")

        self.logger.error(f"GUI DIR: {self.gui_dir}")

        self.flask_server = Server(
            frontend_path=self.gui_dir, application=self.application, queue=queue
        )

        stream = StringIO()
        with redirect_stdout(stream):
            self.window = webview.create_window(
                window_name, self.flask_server.flask_app, http_port=port
            )

        if token:
            webview.token = token

        try:
            self._work(debug=debug)
        except Exception as e:
            self.logger.error(f"pywebview process encountered exception: {e}")
        finally:
            self.socket.close()
            self.context.term()

    def _work(self, debug: bool):
        webview.start(debug=debug, private_mode=False)

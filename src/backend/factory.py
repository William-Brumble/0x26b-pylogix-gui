import os
import webview
from flask import Flask
from io import StringIO
from contextlib import redirect_stdout
from logging import getLogger, NullHandler, StreamHandler, DEBUG, Formatter

from app import App
from server import Server

logger = getLogger(__name__)
logger.addHandler(NullHandler())

class Factory:

    @staticmethod
    def create_root_logger():
        root_logger = getLogger()
        root_logger.addHandler(NullHandler())
        root_logger.setLevel(DEBUG)
        return root_logger

    @staticmethod
    def create_stream_logger(logger):
        ch = StreamHandler()
        ch.setLevel(DEBUG)
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    @staticmethod
    def create_app(simulate: bool = False):
        logger.debug(f"Creating the app with simulate: {simulate}")
        application = App(simulate=simulate)
        return application

    @staticmethod
    def create_server(application: App):
        logger.debug(f"Creating the server with application: {application}")

        gui_dir = os.path.join(os.path.dirname(__file__), 'dist')  # development path
        logger.debug(f"gui_dir set to: {gui_dir}")

        flask_server = Server(frontend_path=gui_dir, application=application)

        return flask_server

    @staticmethod
    def create_window(server: Flask, server_port: int, window_name: str):
        logger.debug(f"Creating the window with server: {server}, and window_name: {window_name}")
        stream = StringIO()
        with redirect_stdout(stream):
            window = webview.create_window(window_name, server, http_port=server_port)

        return window


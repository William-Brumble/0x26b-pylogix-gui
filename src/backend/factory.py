import os
import webview
from flask import Flask
from io import StringIO
from contextlib import redirect_stdout
from logging import getLogger, NullHandler

logger = getLogger(__name__)
logger.addHandler(NullHandler())

from app import App
from server import Server

class Factory:

    @staticmethod
    def create_app(simulate: bool = False):
        application = App(simulate=simulate)
        return application

    @staticmethod
    def create_server(application: App):
        gui_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')  # development path

        if not os.path.exists(gui_dir):  # frozen executable path
            gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend')

        flask_server = Server(frontend_path=gui_dir, application=application)

        return flask_server

    @staticmethod
    def create_window(server: Flask, window_name: str):
        stream = StringIO()
        with redirect_stdout(stream):
            window = webview.create_window(window_name, server)
        return window


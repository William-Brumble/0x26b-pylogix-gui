import os
import webview
from flask import Flask
from io import StringIO
from contextlib import redirect_stdout
from logging import getLogger, NullHandler

logger = getLogger()
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

        flask_server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
        flask_server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
        flask_server.after_request(f=Server.add_header)
        flask_server.add_url_rule(rule="/", view_func=Server.landing, methods=["POST"])
        flask_server.add_url_rule(rule="/init", view_func=Server.initialize, methods=["GET"])
        flask_server.add_url_rule(rule="/connect", view_func=Server.connect, methods=["GET"])
        flask_server.add_url_rule(rule="/close", view_func=Server.close, methods=["GET"])
        flask_server.add_url_rule(rule="/get-connection-size", view_func=Server.get_connection_size, methods=["GET"])
        flask_server.add_url_rule(rule="/set-connection-size", view_func=Server.set_connection_size, methods=["GET"])
        flask_server.add_url_rule(rule="/read", view_func=Server.read, methods=["GET"])
        flask_server.add_url_rule(rule="/write", view_func=Server.write, methods=["POST"])
        flask_server.add_url_rule(rule="/get-plc-time", view_func=Server.get_plc_time, methods=["GET"])
        flask_server.add_url_rule(rule="/set-plc-time", view_func=Server.set_plc_time, methods=["POST"])
        flask_server.add_url_rule(rule="/get-tag-list", view_func=Server.get_tag_list, methods=["GET"])
        flask_server.add_url_rule(rule="/get-program-tag-list", view_func=Server.get_program_tag_list, methods=["GET"])
        flask_server.add_url_rule(rule="/get-programs-list", view_func=Server.get_programs_list, methods=["GET"])
        flask_server.add_url_rule(rule="/discover", view_func=Server.discover, methods=["GET"])
        flask_server.add_url_rule(rule="/get-module-properties", view_func=Server.get_module_properties, methods=["GET"])
        flask_server.add_url_rule(rule="/get-device-propreties", view_func=Server.get_device_properties, methods=["GET"])

        Server.application = application

        return flask_server

    @staticmethod
    def create_window(server: Flask, window_name: str):
        stream = StringIO()
        with redirect_stdout(stream):
            window = webview.create_window(window_name, server)
        return window


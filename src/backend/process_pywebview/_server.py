import webview
from dataclasses import asdict
from flask import Flask, jsonify, render_template, request, Response
from flask_cors import CORS
from logging import getLogger, NullHandler, DEBUG
from logging.handlers import QueueHandler
import multiprocessing

from process_pywebview._app import App
from process_pywebview._models import *
from process_pywebview._utils import *


class Server:
    def __init__(
        self,
        frontend_path: str,
        application: App,
        queue: multiprocessing.Queue = None,
    ):
        self.flask_app = Flask(
            __name__, static_folder=frontend_path, template_folder=frontend_path
        )
        self._logger = getLogger("pywebview-server")
        self._logger.setLevel(DEBUG)
        self._logger.addHandler(NullHandler())
        if queue:
            self.handler = QueueHandler(queue)
            self._logger.addHandler(self.handler)

        self.flask_app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1  # disable caching
        self.application = application
        self.cors = CORS(self.flask_app, resources={r"/*": {"origins": "*"}})

        """ Defining routes in init for simple way to wrap flask in a class """

        @self.flask_app.after_request
        def __add_header(response):
            return self.add_header(response)

        @self.flask_app.route("/")
        def __landing():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask landing route fired")
            return self.landing()

        @self.flask_app.route("/connect", methods=["POST"])
        def __connect():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask connect route fired")
            return self.connect()

        @self.flask_app.route("/close", methods=["POST"])
        def __close():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask close route fired")
            return self.close()

        @self.flask_app.route("/get-connection-size", methods=["POST"])
        def __get_connection_size():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get connection size route fired")
            return self.get_connection_size()

        @self.flask_app.route("/set-connection-size", methods=["POST"])
        def __set_connection_size():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask set connection size route fired")
            return self.set_connection_size()

        @self.flask_app.route("/read", methods=["POST"])
        def __read():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask read route fired")
            return self.read()

        @self.flask_app.route("/write", methods=["POST"])
        def __write():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask write route fired")
            return self.write()

        @self.flask_app.route("/get-plc-time", methods=["POST"])
        def __get_plc_time():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get plc time route fired")
            return self.get_plc_time()

        @self.flask_app.route("/set-plc-time", methods=["POST"])
        def __set_plc_time():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask set plc time route fired")
            return self.set_plc_time()

        @self.flask_app.route("/get-tag-list", methods=["POST"])
        def __get_tag_list():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get tag list route fired")
            return self.get_tag_list()

        @self.flask_app.route("/get-program-tag-list", methods=["POST"])
        def __get_program_tag_list():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get program tag list route fired")
            return self.get_program_tag_list()

        @self.flask_app.route("/get-programs-list", methods=["POST"])
        def __get_programs_list():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get programs list route fired")
            return self.get_programs_list()

        @self.flask_app.route("/discover", methods=["POST"])
        def __discover():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask discover route fired")
            return self.discover()

        @self.flask_app.route("/get-module-properties", methods=["POST"])
        def __get_module_properties():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get module properties route fired")
            return self.get_module_properties()

        @self.flask_app.route("/get-device-properties", methods=["POST"])
        def __get_device_properties():
            self._logger.debug("-" * 80)
            self._logger.debug("Flask get device properties route fired")
            return self.get_device_properties()

    def add_header(self, response):
        self._logger.debug(f"Add header wrapper called with: {response}")

        response.headers["Cache-Control"] = "no-store"

        self._logger.debug(f"Wrapper response: {response}")
        return response

    def landing(self) -> str:
        return render_template("index.html", token=webview.token)

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(Connect)
    def connect(self, request: Connect) -> Response:
        response = self.application.connect(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    def close(self) -> Response:
        response = self.application.close()
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    def get_connection_size(self) -> Response:
        response = self.application.get_connection_size()
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(ConnectionSize)
    def set_connection_size(self, request: ConnectionSize) -> Response:
        response = self.application.set_connection_size(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(Read)
    def read(self, request: Read) -> Response:
        response = self.application.read(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(Write)
    def write(self, request: Write) -> Response:
        response = self.application.write(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(PlcTime)
    def get_plc_time(self, request: PlcTime) -> Response:
        response = self.application.get_plc_time(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    def set_plc_time(self) -> Response:
        response = self.application.set_plc_time()
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(TagList)
    def get_tag_list(self, request: TagList) -> Response:
        response = self.application.get_tag_list(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(ProgramTagList)
    def get_program_tag_list(self, request: ProgramTagList) -> Response:
        response = self.application.get_program_tag_list(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    def get_programs_list(self) -> Response:
        response = self.application.get_programs_list()
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    def discover(self) -> Response:
        response = self.application.discover()
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(ModuleProperties)
    def get_module_properties(self, request: ModuleProperties) -> Response:
        response = self.application.get_module_properties(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    def get_device_properties(self) -> Response:
        response = self.application.get_device_properties()
        return jsonify(asdict(response))

import json
import webview
from dataclasses import asdict
from flask import Flask, jsonify, render_template, request, Response
from flask_cors import CORS
from logging import getLogger, NullHandler

from app import App
from utils import *
from models import *

logger = getLogger(__name__)
logger.addHandler(NullHandler())

class Server:

    def __init__(self, frontend_path: str, application: App):
        self.flask_app = Flask(__name__, static_folder=frontend_path, template_folder=frontend_path)
        self.flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
        self.application = application
        self.cors = CORS(self.flask_app, resources={r"/*": {"origins": "*"}})

        """ Defining routes in init for simple way to wrap flask in a class """

        @self.flask_app.after_request
        def __add_header(response):
            return self.add_header(response)

        @self.flask_app.route("/")
        def __landing():
            logger.debug("-" * 80)
            logger.debug("Flask landing route fired")
            return self.landing()

        @self.flask_app.route("/connect", methods = ['POST'])
        def __connect():
            logger.debug("-" * 80)
            logger.debug("Flask connect route fired")
            return self.connect()

        @self.flask_app.route("/close", methods = ['POST'])
        def __close():
            logger.debug("-" * 80)
            logger.debug("Flask close route fired")
            return self.close()

        @self.flask_app.route("/get-connection-size", methods = ['POST'])
        def __get_connection_size():
            logger.debug("-" * 80)
            logger.debug("Flask get connection size route fired")
            return self.get_connection_size()

        @self.flask_app.route("/set-connection-size", methods = ['POST'])
        def __set_connection_size():
            logger.debug("-" * 80)
            logger.debug("Flask set connection size route fired")
            return self.set_connection_size()

        @self.flask_app.route("/read", methods = ['POST'])
        def __read():
            logger.debug("-" * 80)
            logger.debug("Flask read route fired")
            return self.read()

        @self.flask_app.route("/write", methods = ['POST'])
        def __write():
            logger.debug("-" * 80)
            logger.debug("Flask write route fired")
            return self.write()

        @self.flask_app.route("/get-plc-time", methods = ['POST'])
        def __get_plc_time():
            logger.debug("-" * 80)
            logger.debug("Flask get plc time route fired")
            return self.get_plc_time()

        @self.flask_app.route("/set-plc-time", methods = ['POST'])
        def __set_plc_time():
            logger.debug("-" * 80)
            logger.debug("Flask set plc time route fired")
            return self.set_plc_time()

        @self.flask_app.route("/get-tag-list", methods = ['POST'])
        def __get_tag_list():
            logger.debug("-" * 80)
            logger.debug("Flask get tag list route fired")
            return self.get_tag_list()

        @self.flask_app.route("/get-program-tag-list", methods = ['POST'])
        def __get_program_tag_list():
            logger.debug("-" * 80)
            logger.debug("Flask get program tag list route fired")
            return self.get_program_tag_list()

        @self.flask_app.route("/get-programs-list", methods = ['POST'])
        def __get_programs_list():
            logger.debug("-" * 80)
            logger.debug("Flask get programs list route fired")
            return self.get_programs_list()

        @self.flask_app.route("/discover", methods = ['POST'])
        def __discover():
            logger.debug("-" * 80)
            logger.debug("Flask discover route fired")
            return self.discover()

        @self.flask_app.route("/get-module-properties", methods = ['POST'])
        def __get_module_properties():
            logger.debug("-" * 80)
            logger.debug("Flask get module properties route fired")
            return self.get_module_properties()

        @self.flask_app.route("/get-device-properties", methods = ['POST'])
        def __get_device_properties():
            logger.debug("-" * 80)
            logger.debug("Flask get device properties route fired")
            return self.get_device_properties()

    def add_header(self, response):
        logger.debug(f"Add header wrapper called with: {response}")

        response.headers['Cache-Control'] = 'no-store'

        logger.debug(f"Wrapper response: {response}")
        return response

    def landing(self) -> str:
        return render_template('index.html', token=webview.token)

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(ConnectReqDTO)
    def connect(self, request: ConnectReqDTO) -> Response:
        response = self.application.connect(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(CloseReqDTO)
    def close(self, request: CloseReqDTO) -> Response:
        response = self.application.close(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetConnectionSizeReqDTO)
    def get_connection_size(self, request: GetConnectionSizeReqDTO) -> Response:
        response = self.application.get_connection_size(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(SetConnectionSizeReqDTO)
    def set_connection_size(self, request: SetConnectionSizeReqDTO) -> Response:
        response = self.application.set_connection_size(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(ReadReqDTO)
    def read(self, request: ReadReqDTO) -> Response:
        response = self.application.read(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(WriteReqDTO)
    def write(self, request: WriteReqDTO) -> Response:
        response = self.application.write(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetPlcTimeReqDTO)
    def get_plc_time(self, request: GetPlcTimeReqDTO) -> Response:
        response = self.application.get_plc_time(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(SetPlcTimeReqDTO)
    def set_plc_time(self, request: SetPlcTimeReqDTO) -> Response:
        response = self.application.set_plc_time(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetTagListReqDTO)
    def get_tag_list(self, request: GetTagListReqDTO) -> Response:
        response = self.application.get_tag_list(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetProgramTagListReqDTO)
    def get_program_tag_list(self, request: GetProgramTagListReqDTO) -> Response:
        response = self.application.get_program_tag_list(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetProgramsListReqDTO)
    def get_programs_list(self, request: GetProgramsListReqDTO) -> Response:
        response = self.application.get_programs_list(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(DiscoverReqDTO)
    def discover(self, request: DiscoverReqDTO) -> Response:
        response = self.application.discover(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetModulePropertiesReqDTO)
    def get_module_properties(self, request: GetModulePropertiesReqDTO) -> Response:
        response = self.application.get_module_properties(request=request)
        return jsonify(asdict(response))

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetDevicePropertiesReqDTO)
    def get_device_properties(self) -> Response:
        response = self.application.get_device_properties(request=request)
        return jsonify(asdict(response))

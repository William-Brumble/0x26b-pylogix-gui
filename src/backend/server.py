import json
import webview
from dataclasses import asdict
from flask import Flask, jsonify, render_template, request, Response
from flask_cors import CORS
from logging import getLogger, NullHandler

from app import App
from utils import (
        common_exception_handler, 
        common_payload_protection,
        common_token_protection
)
from models import (
        ConnectReqDTO,
        CloseReqDTO,
        GetConnectionSizeReqDTO,
        SetConnectionSizeReqDTO,
        ReadReqDTO,
        WriteReqDTO,
        GetPlcTimeReqDTO,
        SetPlcTimeReqDTO,
        GetTagListReqDTO,
        GetProgramTagListReqDTO,
        GetProgramsListReqDTO,
        DiscoverReqDTO,
        GetModulePropertiesReqDTO,
        GetDevicePropertiesReqDTO
)

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
    def connect(self) -> Response:

        response = self._process_request(
            ConnectReqDTO,
            self.application.connect
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(CloseReqDTO)
    def close(self) -> Response:

        response = self._process_request(
            CloseReqDTO,
            self.application.close
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetConnectionSizeReqDTO)
    def get_connection_size(self) -> Response:

        response = self._process_request(
            GetConnectionSizeReqDTO,
            self.application.get_connection_size
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(SetConnectionSizeReqDTO)
    def set_connection_size(self) -> Response:

        response = self._process_request(
            SetConnectionSizeReqDTO,
            self.application.set_connection_size
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(ReadReqDTO)
    def read(self) -> Response:

        response = self._process_request(
            ReadReqDTO,
            self.application.read
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(WriteReqDTO)
    def write(self) -> Response:

        response = self._process_request(
            WriteReqDTO,
            self.application.write
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetPlcTimeReqDTO)
    def get_plc_time(self) -> Response:

        response = self._process_request(
            GetPlcTimeReqDTO,
            self.application.get_plc_time
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(SetPlcTimeReqDTO)
    def set_plc_time(self) -> Response:

        response = self._process_request(
            SetPlcTimeReqDTO,
            self.application.set_plc_time
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetTagListReqDTO)
    def get_tag_list(self) -> Response:

        response = self._process_request(
            GetTagListReqDTO,
            self.application.get_tag_list
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetProgramTagListReqDTO)
    def get_program_tag_list(self) -> Response:

        response = self._process_request(
            GetProgramTagListReqDTO,
            self.application.get_program_tag_list
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetProgramsListReqDTO)
    def get_programs_list(self) -> Response:

        response = self._process_request(
            GetProgramsListReqDTO,
            self.application.get_programs_list
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(DiscoverReqDTO)
    def discover(self) -> Response:

        response = self._process_request(
            DiscoverReqDTO,
            self.application.discover
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetModulePropertiesReqDTO)
    def get_module_properties(self) -> Response:

        response = self._process_request(
            GetModulePropertiesReqDTO,
            self.application.get_module_properties
        )

        return response

    @common_exception_handler
    @common_token_protection
    @common_payload_protection(GetDevicePropertiesReqDTO)
    def get_device_properties(self) -> Response:

        response = self._process_request(
            GetDevicePropertiesReqDTO,
            self.application.get_device_properties
        )

        return response

    def _process_request(self, RequestClass, procedural_parameter):
        logger.debug(f"Process request called with class: {RequestClass}, procedural_parameter: {procedural_parameter}")

        logger.debug(f"Checking to see if application is initialized")
        if self.application:
            logger.debug(f"Application is initialized")

            data = json.loads(request.data)
            logger.debug(f"Parsed the request data, got: {data}")

            payload = RequestClass(**data)
            logger.debug(f"Instantiated request class: {payload}")

            response = procedural_parameter(payload)
            logger.debug(f"Processed the request, got response: {response}")

            return jsonify(asdict(response))
        else:
            logger.debug(f"Application is not initialized")
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")


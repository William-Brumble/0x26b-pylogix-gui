import json
import webview
from dataclasses import asdict
from flask import Flask, jsonify, render_template, request, Response
from logging import getLogger, NullHandler

from models import (
        StatusDTO,
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
        GetDevicePropertiesReqDTO,
)
from app import App

logger = getLogger(__name__)
logger.addHandler(NullHandler())

def common_token_protection(f):
    """ Returns error message if browser token doesn't match application token """
    def wrap(self, *args, **kwargs):
        data = json.loads(request.data)
        token = data.get('token')
        if token == webview.token:
            return f(self, *args, **kwargs)
        else:
            payload = StatusDTO(status="401 Unauthorized", error=True, error_message="Incorrect token supplied")
            return jsonify(asdict(payload))
    return wrap

def common_payload_protection(PayloadClass):
    """ Returns error message if the json payload doesn't match what's required """
    def wrap(f):
        def modified_f(*args, **kwargs):
            try:
                data = json.loads(request.data)
                PayloadClass(**data)
                return f(*args, **kwargs)
            except TypeError:
                return PayloadClass(error=True, status="400 Bad Request", error_message="Incorrect json data")
        return modified_f
    return wrap

class Server:

    def __init__(self, frontend_path: str, application: App):
        self.flask_app = Flask(__name__, static_folder=frontend_path, template_folder=frontend_path)
        self.flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
        self.application = application

        """ Defining routes in init for simple way to wrap flask in a class """
        @self.flask_app.after_request
        def __add_header(response):
            return self.add_header(response)

        @self.flask_app.route("/")
        def __landing():
            return self.landing()

        @self.flask_app.route("/init")
        @common_token_protection
        def __initialize():
            return self.initialize()

        @self.flask_app.route("/connect")
        def __connect():
            return self.connect()

        @self.flask_app.route("/close")
        def __close():
            return self.close()

        @self.flask_app.route("/get-connectio-size")
        def __get_connection_size():
            return self.get_connection_size()

        @self.flask_app.route("/set-connection-size")
        def __set_connection_size():
            return self.set_connection_size()

        @self.flask_app.route("/read")
        def __read():
            return self.read()

        @self.flask_app.route("/write")
        def __write():
            return self.write()

        @self.flask_app.route("/get-plc-time")
        def __get_plc_time():
            return self.get_plc_time()

        @self.flask_app.route("/set-plc-time")
        def __set_plc_time():
            return self.set_plc_time()

        @self.flask_app.route("/get-tag-list")
        def __get_tag_list():
            return self.get_tag_list()

        @self.flask_app.route("/get-program-tag-list")
        def __get_program_tag_list():
            return self.get_program_tag_list()

        @self.flask_app.route("/get_programs_list")
        def __get_programs_list():
            return self.get_programs_list()

        @self.flask_app.route("/discover")
        def __discover():
            return self.discover()

        @self.flask_app.route("/get-module-properties")
        def __get_module_properties():
            return self.get_module_properties()

        @self.flask_app.route("/get-device-properties")
        def __get_device_properties():
            return self.get_device_properties()


    def add_header(self, response):
        response.headers['Cache-Control'] = 'no-store'
        return response


    def landing(self) -> str:
        """
        Render index.html. Initialization is performed asynchronously in initialize() function
        """
        return render_template('index.html', token=webview.token)


    def initialize(self) -> Response:
        if self.application:
            can_start = self.application.initialize()

            if can_start:
                response = {
                    'status': 'ok',
                }
            else:
                response = {'status': 'error'}

            return jsonify(response)
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(ConnectReqDTO)
    def connect(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = ConnectReqDTO(**data)
            response = self.application.connect(payload)
            return jsonify(asdict(response))
        else:
            print("No application!")
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(CloseReqDTO)
    def close(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = CloseReqDTO(**data)
            response = self.application.close(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetConnectionSizeReqDTO)
    def get_connection_size(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetConnectionSizeReqDTO(**data)
            response = self.application.get_connection_size(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(SetConnectionSizeReqDTO)
    def set_connection_size(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = SetConnectionSizeReqDTO(**data)
            response = self.application.set_connection_size(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(ReadReqDTO)
    def read(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = ReadReqDTO(**data)
            response = self.application.read(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(WriteReqDTO)
    def write(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = WriteReqDTO(**data)
            response = self.application.write(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetPlcTimeReqDTO)
    def get_plc_time(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetPlcTimeReqDTO(**data)
            response = self.application.get_plc_time(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(SetPlcTimeReqDTO)
    def set_plc_time(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = SetPlcTimeReqDTO(**data)
            response = self.application.set_plc_time(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetTagListReqDTO)
    def get_tag_list(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetTagListReqDTO(**data)
            response = self.application.get_tag_list(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetProgramTagListReqDTO)
    def get_program_tag_list(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetProgramTagListReqDTO(**data)
            response = self.application.get_program_tag_list(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetProgramsListReqDTO)
    def get_programs_list(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetProgramsListReqDTO(**data)
            response = self.application.get_programs_list(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(DiscoverReqDTO)
    def discover(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = DiscoverReqDTO(**data)
            response = self.application.discover(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetModulePropertiesReqDTO)
    def get_module_properties(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetModulePropertiesReqDTO(**data)
            response = self.application.get_module_properties(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @common_token_protection
    @common_payload_protection(GetDevicePropertiesReqDTO)
    def get_device_properties(self) -> Response:
        if self.application:
            data = json.loads(request.data)
            payload = GetDevicePropertiesReqDTO(**data)
            response = self.application.get_device_properties(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")


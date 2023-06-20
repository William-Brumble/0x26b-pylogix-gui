import json
import webview
from dataclasses import asdict
from flask import Flask, jsonify, render_template, request, Response
from logging import getLogger, NullHandler

from app import App
from utils import common_exception_handler
from models import (
        StatusDTO,
        ConnectReqDTO, ConnectResDTO,
        CloseReqDTO, CloseResDTO,
        GetConnectionSizeReqDTO, GetConnectionSizeResDTO,
        SetConnectionSizeReqDTO, SetConnectionSizeResDTO,
        ReadReqDTO, ReadResDTO,
        WriteReqDTO, WriteResDTO,
        GetPlcTimeReqDTO, GetPlcTimeResDTO,
        SetPlcTimeReqDTO, SetPlcTimeResDTO,
        GetTagListReqDTO, GetTagListResDTO,
        GetProgramTagListReqDTO, GetProgramTagListResDTO,
        GetProgramsListReqDTO, GetProgramsListResDTO,
        DiscoverReqDTO, DiscoverResDTO,
        GetModulePropertiesReqDTO, GetModulePropertiesResDTO,
        GetDevicePropertiesReqDTO, GetDevicePropertiesResDTO
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

def common_token_protection(f):
    """ Returns error message if browser token doesn't match application token """
    def wrap(self, *args, **kwargs):
        logger.debug("Checking to see if token in the request matches the server token")

        logger.debug(f"request.data: {request.data}")
        data = json.loads(request.data)

        token = data.get('token')
        logger.debug(f"Request token: {token}")
        logger.debug(f"Server token: {webview.token}")

        if token == webview.token:
            logger.debug("Token matches all is well")
            return f(self, *args, **kwargs)
        else:
            logger.error("The request token doesn't match the server token")
            payload = StatusDTO(status="401 Unauthorized", error=True, error_message="Incorrect token supplied")
            return jsonify(asdict(payload))
    return wrap

def common_payload_protection(PayloadClass):
    """ Returns error message if the json payload doesn't match what's required """
    def wrap(f):
        def modified_f(*args, **kwargs):
            logger.debug("Checking to see if the payload in the request matches what the route needs")
            try:
                data = json.loads(request.data)
                PayloadClass(**data)
                logger.debug("Payload matches all is well")
                return f(*args, **kwargs)
            except TypeError:
                logger.error("The payload in the request doesn't match what's needed by the route")
                payload = StatusDTO(error=True, status="400 Bad Request", error_message="Incorrect json data")
                return jsonify(asdict(payload))
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
            logger.debug("Flask add header route fired")
            return self.add_header(response)

        @self.flask_app.route("/", methods = ['GET'])
        def __landing():
            logger.debug("Flask landing route fired")
            return self.landing()

        @self.flask_app.route("/init", methods = ['GET'])
        def __initialize():
            logger.debug("Flask initialize route fired")
            return self.initialize()

        @self.flask_app.route("/connect", methods = ['GET'])
        def __connect():
            logger.debug("Flask connect route fired")
            return self.connect()

        @self.flask_app.route("/close", methods = ['GET'])
        def __close():
            logger.debug("Flask close route fired")
            return self.close()

        @self.flask_app.route("/get-connection-size", methods = ['GET'])
        def __get_connection_size():
            logger.debug("Flask get connection size route fired")
            return self.get_connection_size()

        @self.flask_app.route("/set-connection-size", methods = ['POST'])
        def __set_connection_size():
            logger.debug("Flask set connection size route fired")
            return self.set_connection_size()

        @self.flask_app.route("/read", methods = ['GET'])
        def __read():
            logger.debug("Flask read route fired")
            return self.read()

        @self.flask_app.route("/write", methods = ['POST'])
        def __write():
            logger.debug("Flask write route fired")
            return self.write()

        @self.flask_app.route("/get-plc-time", methods = ['GET'])
        def __get_plc_time():
            logger.debug("Flask get plc time route fired")
            return self.get_plc_time()

        @self.flask_app.route("/set-plc-time", methods = ['POST'])
        def __set_plc_time():
            logger.debug("Flask set plc time route fired")
            return self.set_plc_time()

        @self.flask_app.route("/get-tag-list", methods = ['GET'])
        def __get_tag_list():
            logger.debug("Flask get tag list route fired")
            return self.get_tag_list()

        @self.flask_app.route("/get-program-tag-list", methods = ['GET'])
        def __get_program_tag_list():
            logger.debug("Flask get program tag list route fired")
            return self.get_program_tag_list()

        @self.flask_app.route("/get_programs_list", methods = ['GET'])
        def __get_programs_list():
            logger.debug("Flask get programs list route fired")
            return self.get_programs_list()

        @self.flask_app.route("/discover", methods = ['GET'])
        def __discover():
            logger.debug("Flask discover route fired")
            return self.discover()

        @self.flask_app.route("/get-module-properties", methods = ['GET'])
        def __get_module_properties():
            logger.debug("Flask get module properties route fired")
            return self.get_module_properties()

        @self.flask_app.route("/get-device-properties", methods = ['GET'])
        def __get_device_properties():
            logger.debug("Flask get device properties route fired")
            return self.get_device_properties()


    def add_header(self, response):
        logger.debug(f"Add header wrapper called with: {response}")
        response.headers['Cache-Control'] = 'no-store'
        logger.debug(f"Wrapper response: {response}")
        return response


    def landing(self) -> str:
        return render_template('index.html', token=webview.token)


    @common_token_protection
    def initialize(self) -> Response:
        logger.debug("Initialize method checking for server application")
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
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(ConnectResDTO)
    @common_token_protection
    @common_payload_protection(ConnectReqDTO)
    def connect(self) -> Response:
        logger.debug("Connect method checking for server application")
        if self.application:

            logger.debug("Server application was initialized")
            data = json.loads(request.data)

            logger.debug(f"Request json data: {data}")
            payload = ConnectReqDTO(**data)

            response = self.application.connect(payload)
            logger.debug(f"Server application response data: {response}")

            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(CloseResDTO)
    @common_token_protection
    @common_payload_protection(CloseReqDTO)
    def close(self) -> Response:
        logger.debug("Close method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = CloseReqDTO(**data)
            response = self.application.close(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetConnectionSizeResDTO)
    @common_token_protection
    @common_payload_protection(GetConnectionSizeReqDTO)
    def get_connection_size(self) -> Response:
        logger.debug("Get connection size method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetConnectionSizeReqDTO(**data)
            response = self.application.get_connection_size(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(SetConnectionSizeResDTO)
    @common_token_protection
    @common_payload_protection(SetConnectionSizeReqDTO)
    def set_connection_size(self) -> Response:
        logger.debug("Set connection size method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = SetConnectionSizeReqDTO(**data)
            response = self.application.set_connection_size(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(ReadResDTO)
    @common_token_protection
    @common_payload_protection(ReadReqDTO)
    def read(self) -> Response:
        logger.debug("Read method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = ReadReqDTO(**data)
            response = self.application.read(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(WriteResDTO)
    @common_token_protection
    @common_payload_protection(WriteReqDTO)
    def write(self) -> Response:
        logger.debug("Write method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = WriteReqDTO(**data)
            response = self.application.write(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetPlcTimeResDTO)
    @common_token_protection
    @common_payload_protection(GetPlcTimeReqDTO)
    def get_plc_time(self) -> Response:
        logger.debug("Get plc time method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetPlcTimeReqDTO(**data)
            response = self.application.get_plc_time(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(SetPlcTimeResDTO)
    @common_token_protection
    @common_payload_protection(SetPlcTimeReqDTO)
    def set_plc_time(self) -> Response:
        logger.debug("Set plc time method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = SetPlcTimeReqDTO(**data)
            response = self.application.set_plc_time(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetTagListResDTO)
    @common_token_protection
    @common_payload_protection(GetTagListReqDTO)
    def get_tag_list(self) -> Response:
        logger.debug("Get tag list method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetTagListReqDTO(**data)
            response = self.application.get_tag_list(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetProgramTagListResDTO)
    @common_token_protection
    @common_payload_protection(GetProgramTagListReqDTO)
    def get_program_tag_list(self) -> Response:
        logger.debug("Get program tag list method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetProgramTagListReqDTO(**data)
            response = self.application.get_program_tag_list(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetProgramsListResDTO)
    @common_token_protection
    @common_payload_protection(GetProgramsListReqDTO)
    def get_programs_list(self) -> Response:
        logger.debug("Get programs list method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetProgramsListReqDTO(**data)
            response = self.application.get_programs_list(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(DiscoverResDTO)
    @common_token_protection
    @common_payload_protection(DiscoverReqDTO)
    def discover(self) -> Response:
        logger.debug("Discover method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = DiscoverReqDTO(**data)
            response = self.application.discover(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetModulePropertiesResDTO)
    @common_token_protection
    @common_payload_protection(GetModulePropertiesReqDTO)
    def get_module_properties(self) -> Response:
        logger.debug("Get module properties method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetModulePropertiesReqDTO(**data)
            response = self.application.get_module_properties(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")

    @common_exception_handler(GetDevicePropertiesResDTO)
    @common_token_protection
    @common_payload_protection(GetDevicePropertiesReqDTO)
    def get_device_properties(self) -> Response:
        logger.debug("Get device properties method checking for server application")
        if self.application:
            data = json.loads(request.data)
            payload = GetDevicePropertiesReqDTO(**data)
            response = self.application.get_device_properties(payload)
            return jsonify(asdict(response))
        else:
            logger.error("Server application object uninitialized")
            raise Exception("Server application object uninitialized")


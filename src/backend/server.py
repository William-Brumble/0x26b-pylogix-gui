import json
import webview
from dataclasses import asdict
from flask import jsonify, render_template, request, Response
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

logger = getLogger()
logger.addHandler(NullHandler())

def common_token_protection(f):
    """ Returns error message if browser token doesn't match application token """
    def wrap(cls, *args, **kwargs):
        data = json.loads(request.data)
        token = data.get('token')
        if token == webview.token:
            return f(cls, *args, **kwargs)
        else:
            payload = StatusDTO(status="401 Unauthorized", error=True, error_message="Incorrect token supplied")
            return jsonify(asdict(payload))
    return wrap

def common_payload_protection(PayloadClass):
    """ Returns error message if the json payload doesn't match what's required """
    def wrap(f):
        def modified_f(cls, *args, **kwargs):
            try:
                data = json.loads(request.data)
                PayloadClass(**data)
                return f(cls, *args, **kwargs)
            except TypeError:
                return PayloadClass(error=True, status="400 Bad Request", error_message="Incorrect json data")
        return modified_f
    return wrap

class Server:

    application: App | None

    @staticmethod
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store'
        return response


    @classmethod
    def landing(cls) -> str:
        """
        Render index.html. Initialization is performed asynchronously in initialize() function
        """
        return render_template('index.html', token=webview.token)


    @classmethod
    @common_token_protection
    def initialize(cls) -> Response:
        if cls.application:
            can_start = cls.application.initialize()

            if can_start:
                response = {
                    'status': 'ok',
                }
            else:
                response = {'status': 'error'}

            return jsonify(response)
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(ConnectReqDTO)
    def connect(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = ConnectReqDTO(**data)
            response = cls.application.connect(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(CloseReqDTO)
    def close(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = CloseReqDTO(**data)
            response = cls.application.close(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetConnectionSizeReqDTO)
    def get_connection_size(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetConnectionSizeReqDTO(**data)
            response = cls.application.get_connection_size(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(SetConnectionSizeReqDTO)
    def set_connection_size(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = SetConnectionSizeReqDTO(**data)
            response = cls.application.set_connection_size(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(ReadReqDTO)
    def read(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = ReadReqDTO(**data)
            response = cls.application.read(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(WriteReqDTO)
    def write(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = WriteReqDTO(**data)
            response = cls.application.write(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetPlcTimeReqDTO)
    def get_plc_time(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetPlcTimeReqDTO(**data)
            response = cls.application.get_plc_time(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(SetPlcTimeReqDTO)
    def set_plc_time(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = SetPlcTimeReqDTO(**data)
            response = cls.application.set_plc_time(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetTagListReqDTO)
    def get_tag_list(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetTagListReqDTO(**data)
            response = cls.application.get_tag_list(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetProgramTagListReqDTO)
    def get_program_tag_list(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetProgramTagListReqDTO(**data)
            response = cls.application.get_program_tag_list(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetProgramsListReqDTO)
    def get_programs_list(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetProgramsListReqDTO(**data)
            response = cls.application.get_programs_list(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(DiscoverReqDTO)
    def discover(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = DiscoverReqDTO(**data)
            response = cls.application.discover(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetModulePropertiesReqDTO)
    def get_module_properties(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetModulePropertiesReqDTO(**data)
            response = cls.application.get_module_properties(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")

    @classmethod
    @common_token_protection
    @common_payload_protection(GetDevicePropertiesReqDTO)
    def get_device_properties(cls) -> Response:
        if cls.application:
            data = json.loads(request.data)
            payload = GetDevicePropertiesReqDTO(**data)
            response = cls.application.get_device_properties(payload)
            return jsonify(asdict(response))
        else:
            raise Exception("Server application object uninitialized")


import json
import os
import webbrowser
from functools import wraps
from flask import Flask, jsonify, render_template, request
import webview
from logging import getLogger, NullHandler

logger = getLogger()
logger.addHandler(NullHandler())

from .app import App

def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data = json.loads(request.data)
        token = data.get('token')
        if token == webview.token:
            return function(*args, **kwargs)
        else:
            raise Exception('Authentication error')

    return wrapper

class Server:

    application: App | None

    @staticmethod
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store'
        return response


    @classmethod
    def landing(cls):
        """
        Render index.html. Initialization is performed asynchronously in initialize() function
        """
        return render_template('index.html', token=webview.token)


    @classmethod
    @verify_token
    def initialize(cls):
        """
        Perform heavy-lifting initialization asynchronously.
        :return:
        """
        can_start = app.initialize()

        if can_start:
            response = {
                'status': 'ok',
            }
        else:
            response = {'status': 'error'}

        return jsonify(response)

    @classmethod
    @verify_token
    def connect(cls):
        return jsonify()

    @classmethod
    @verify_token
    def close(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_connection_size(cls):
        return jsonify()

    @classmethod
    @verify_token
    def set_connection_size(cls):
        return jsonify()

    @classmethod
    @verify_token
    def read(cls):
        return jsonify()

    @classmethod
    @verify_token
    def write(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_plc_time(cls):
        return jsonify()

    @classmethod
    @verify_token
    def set_plc_time(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_tag_list(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_program_tag_list(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_programs_list(cls):
        return jsonify()

    @classmethod
    @verify_token
    def discover(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_module_properties(cls):
        return jsonify()

    @classmethod
    @verify_token
    def get_device_properties(cls):
        return jsonify()

import json
import os
import webbrowser
from functools import wraps

import src.backend.app
from flask import Flask, jsonify, render_template, request

import webview

import logging
logger = logging.getLogger(__name__)

gui_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')  # development path

if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend')

server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching

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


@server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


@server.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html', token=webview.token)


@server.route('/init', methods=['POST'])
@verify_token
def initialize():
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

@server.route('/connect', methods=['GET'])
@verify_token
def connect():
    return jsonify()

@server.route('/close', methods=['GET'])
@verify_token
def close():
    return jsonify()

@server.route('/get-connection-size', methods=['GET'])
@verify_token
def get_connection_size():
    return jsonify()

@server.route('/set-connection-size', methods=['GET'])
@verify_token
def set_connection_size():
    return jsonify()

@server.route('/read', methods=['GET'])
@verify_token
def read():
    return jsonify()

@server.route('/write', methods=['POST'])
@verify_token
def write():
    return jsonify()

@server.route('/get-plc-time', methods=['GET'])
@verify_token
def get_plc_time():
    return jsonify()

@server.route('/set-plc-time', methods=['POST'])
@verify_token
def set_plc_time():
    return jsonify()

@server.route('/get-tag-list', methods=['GET'])
@verify_token
def get_tag_list():
    return jsonify()

@server.route('/get-program-tag-list', methods=['GET'])
@verify_token
def get_program_tag_list():
    return jsonify()

@server.route('/get-programs-list', methods=['GET'])
@verify_token
def get_programs_list():
    return jsonify()

@server.route('/discover', methods=['GET'])
@verify_token
def discover():
    return jsonify()

@server.route('/get-module-properties', methods=['GET'])
@verify_token
def get_module_properties():
    return jsonify()

@server.route('/get-device-properties', methods=['GET'])
@verify_token
def get_device_properties():
    return jsonify()

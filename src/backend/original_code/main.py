import webview
import argparse

from factory import Factory

import os
import sys

# Create the argument parser
parser = argparse.ArgumentParser(description='Pylogix GUI')
parser.add_argument('-p', '--port', default=65535, help='Port for the server to listen on')
parser.add_argument('-t', '--token', default=None, help='The pywebview token')
parser.add_argument('--simulate', action="store_true", help='Simulate a connection to a PLC')
parser.add_argument('--logging', action="store_true", help='Enable debug logging to console')
parser.add_argument('--debug', action="store_true", help='Enable pywebview debug window')
args = parser.parse_args()

def log_startup_information():
    frozen = 'not'
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    logger.info(f"we are {frozen} 'frozen'")
    logger.info(f"bundle dir is {bundle_dir}")
    logger.info(f"sys.argv[0] is {sys.argv[0]}")
    logger.info(f"sys.executable is {sys.executable}")
    logger.info(f"os.getcwd is {os.getcwd()}")

if __name__ == '__main__':
    logger = Factory.create_root_logger()
    if args.logging:
        logger = Factory.create_stream_logger(logger)

    logger.debug("The application had started")

    log_startup_information()

    logger.debug("Using the factory to create the app")
    application = Factory.create_app(simulate=args.simulate)

    logger.debug("Using the factory to create the server")
    server = Factory.create_server(application=application)

    logger.debug("Using the factory to create the window")
    window = Factory.create_window(server=server.flask_app, server_port=args.port, window_name="0x26b-pylogix-gui", token=args.token)

    webview.start(debug=args.debug, private_mode=False)



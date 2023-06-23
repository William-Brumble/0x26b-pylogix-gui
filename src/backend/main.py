import webview

from factory import Factory

import os
import sys


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
    logger = Factory.create_stream_logger(logger)

    logger.debug("The application had started")

    log_startup_information()

    logger.debug("Using the factory to create the app")
    application = Factory.create_app(simulate=True)

    logger.debug("Using the factory to create the server")
    server = Factory.create_server(application=application)

    logger.debug("Using the factory to create the window")
    window = Factory.create_window(server=server.flask_app, server_port=5000, token="test", window_name="pylogix")

    webview.start(debug=True)


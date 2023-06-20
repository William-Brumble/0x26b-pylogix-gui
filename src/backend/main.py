import webview
from logging import getLogger, NullHandler, StreamHandler, DEBUG, Formatter

from factory import Factory

logger = getLogger()
logger.addHandler(NullHandler())
logger.setLevel(DEBUG)

ch = StreamHandler()
ch.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug("TESTING 123")

if __name__ == '__main__':
    logger.debug("The application had started")

    logger.debug("Using the factory to create the app")
    application = Factory.create_app(simulate=True)

    logger.debug("Using the factory to create the server")
    server = Factory.create_server(application=application)

    logger.debug("Using the factory to create the window")
    window = Factory.create_window(server=server.flask_app, server_port=5000, token="test", window_name="pylogix")

    webview.start(debug=True)

import webview
from logging import getLogger, NullHandler

from factory import Factory

logger = getLogger(__name__)
logger.addHandler(NullHandler())

if __name__ == '__main__':

    application = Factory.create_app(simulate=True)
    server = Factory.create_server(application=application)
    window = Factory.create_window(server=server.flask_app, window_name="pylogix")

    webview.token = "test"
    webview.start(debug=True)

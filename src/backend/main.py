import webview
from logging import getLogger, NullHandler

from factory import Factory

logger = getLogger()
logger.addHandler(NullHandler())

if __name__ == '__main__':

    application = Factory.create_app(simulate=True)
    server = Factory.create_server(application=application)
    window = Factory.create_window(server=server, window_name="pylogix")

    webview.start(debug=True)

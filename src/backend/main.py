import logging
from contextlib import redirect_stdout
from io import StringIO

from .server import server

import webview

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('PYLOGIX', server)
        webview.start(debug=True)

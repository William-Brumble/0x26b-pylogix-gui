from flask import jsonify
from dataclasses import asdict
from logging import getLogger, NullHandler

from models import StatusDTO

logger = getLogger()
logger.addHandler(NullHandler())

def common_exception_handler(ResponseClass):
    """ Returns error message if an exception occurs """
    def wrap(f):
        def modified_f(self, *args, **kwargs):
            try:
                return f(self, *args, **kwargs)
            except Exception as e:
                logger.error(f"exception in method {f.__name__}: {e}")
                payload = asdict(
                    StatusDTO(error=True, status="500 Internal Server Error", error_message=str(e))
                )
                return jsonify(payload)
        return modified_f
    return wrap

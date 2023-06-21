import json
import webview
from flask import jsonify, request
from dataclasses import asdict
from logging import getLogger, NullHandler

from models import StatusDTO

logger = getLogger()
logger.addHandler(NullHandler())

def common_exception_handler(f):
    """ Returns error message if an exception occurs """
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

def common_connection_protection(f):
    """ Returns error message if not connected to a PLC """
    def modified_f(self, *args, **kwargs):
        if self._plc is not None:
            return f(self, *args, **kwargs)
        else:
            logger.warning(f"412 Precondition Failed: You must be connected to a PLC before sending a request")
            return StatusDTO(error=True, status="412 Precondition Failed", error_message="You must be connected to a PLC before sending a request")
    return modified_f

def common_payload_protection(PayloadClass):
    """ Returns error message if the json payload doesn't match what's required """
    def wrap(f):
        def modified_f(self, *args, **kwargs):
            logger.debug("Checking to see if the payload in the request matches what the route needs")
            try:
                data = json.loads(request.data)
                PayloadClass(**data)
                logger.debug("Payload matches all is well")
                return f(self, *args, **kwargs)
            except TypeError:
                logger.error("The payload in the request doesn't match what's needed by the route")
                payload = StatusDTO(error=True, status="400 Bad Request", error_message="Incorrect json data")
                return jsonify(asdict(payload))
        return modified_f
    return wrap

def common_token_protection(f):
    """ Returns error message if browser token doesn't match application token """
    def wrap(self, *args, **kwargs):
        logger.debug("Checking to see if token in the request matches the server token")

        data = json.loads(request.data)

        token = data.get('token')
        logger.debug(f"Request token: {token}")
        logger.debug(f"Server token: {webview.token}")

        if token == webview.token:
            logger.debug("Token matches all is well")
            return f(self, *args, **kwargs)
        else:
            logger.error("The request token doesn't match the server token")
            payload = StatusDTO(status="401 Unauthorized", error=True, error_message="Incorrect token supplied")
            return jsonify(asdict(payload))
    return wrap


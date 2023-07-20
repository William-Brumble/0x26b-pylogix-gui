import json
import webview
from flask import jsonify, request, has_request_context, has_app_context
from dataclasses import asdict, fields
from process_pywebview._models import Status


def common_payload_protection(PayloadClass):
    """Returns error message if the json payload doesn't match what's required"""

    def wrap(f):
        def modified_f(self, *args, **kwargs):
            global request

            self._logger.debug(
                "Checking to see if the payload in the request matches what the route needs"
            )
            try:
                payload_class_field_names = [
                    field.name for field in fields(PayloadClass)
                ]
                self._logger.debug(
                    f"Needed payload fields: {payload_class_field_names}"
                )

                if has_app_context() and has_request_context():
                    data = json.loads(request.data)
                else:
                    data = kwargs
                self._logger.debug(f"Request payload: {data}")

                request_payload = PayloadClass(**data)
                self._logger.debug("Payload matches all is well")

                try:
                    response = f(self, *args, request=request_payload)
                    return response
                except Exception as e:
                    self._logger.error(
                        f"Encountered an exception when calling the wrapped function: {e}"
                    )
                    raise e

            except TypeError:
                self._logger.error(
                    "The payload in the request doesn't match what's needed by the route"
                )
                payload = Status(
                    error=True,
                    status="400 Bad Request",
                    error_message="Incorrect json data",
                )

                if has_app_context() and has_request_context():
                    return jsonify(asdict(payload))
                else:
                    return asdict(payload)

        return modified_f

    return wrap


def common_exception_handler(f):
    """Returns error message if an exception occurs"""

    def modified_f(self, *args, **kwargs):
        try:
            return f(self, *args, **kwargs)
        except Exception as e:
            self._logger.error(f"exception in method {f.__name__}: {e}")
            payload = asdict(
                Status(
                    error=True, status="500 Internal Server Error", error_message=str(e)
                )
            )
            return jsonify(payload)

    return modified_f


def common_token_protection(f):
    """Returns error message if browser token doesn't match application token"""

    def wrap(self, *args, **kwargs):
        self._logger.debug(
            "Checking to see if token in the request matches the server token"
        )

        data = json.loads(request.data)

        token = data.get("token")
        self._logger.debug(f"Request token: {token}")
        self._logger.debug(f"Server token: {webview.token}")

        if token == webview.token:
            self._logger.debug("Token matches all is well")
            try:
                return f(self, *args, **kwargs)
            except Exception as e:
                self._logger.error(f"Exception: {e}")
                raise e
        else:
            self._logger.error("The request token doesn't match the server token")
            payload = Status(
                status="401 Unauthorized",
                error=True,
                error_message="The client supplied a token that doesn't match the server's token",
            )
            return jsonify(asdict(payload))

    return wrap

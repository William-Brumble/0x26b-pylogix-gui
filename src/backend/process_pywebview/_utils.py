from dataclasses import asdict, fields

from process_pylogix._models import Status


def common_payload_protection(PayloadClass):
    """Returns error message if the json payload doesn't match what's required"""

    def wrap(f):
        def modified_f(self, *args, **kwargs):
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
                self._logger.debug(f"Received payload: {kwargs}")

                request = PayloadClass(**kwargs)
                self._logger.debug("Payload matches all is well")

                try:
                    response = f(self, *args, request=request)
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
                return asdict(payload)

        return modified_f

    return wrap

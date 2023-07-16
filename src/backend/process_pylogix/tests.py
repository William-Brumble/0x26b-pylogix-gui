import json
import unittest
from dataclasses import asdict

from process_pylogix._models import *
from process_pylogix._pylogix import Pylogix


class IntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pylogix = Pylogix(enable_network=False)
        return super().setUp()

    def test_connect(self):
        payload = {
            "ip_address": "192.168.1.196",
            "slot": 0,
            "timeout": 5,
            "Micro800": False,
        }
        response = self.pylogix._connect(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_close(self):
        response = self.pylogix._close()
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_get_connection_size(self):
        response = self.pylogix._get_connection_size()
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_set_connection_size(self):
        payload = {"connection_size": 508}
        response = self.pylogix._set_connection_size(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_read(self):
        payload = {"tag": "some-tag", "count": 1, "datatype": None}
        response = self.pylogix._read(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertIsInstance(response.response, list)
        for i in response.response:
            self.assertIsInstance(i, Response)
            self.assertIsInstance(i.TagName, str)
            self.assertIsInstance(i.Status, str)
            if i.Value:
                self.assertIsInstance(
                    i.Value,
                    (
                        bool,
                        int,
                        str,
                        list[str],
                        float,
                        datetime,
                        list[Tag],
                        LGXDevice,
                        list[LGXDevice],
                    ),
                )

    def test_write(self):
        payload = {"tag": "some-tag", "value": 619, "datatype": None}
        response = self.pylogix._write(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertIsInstance(response.response, list)
        for i in response.response:
            self.assertIsInstance(i, Response)
            self.assertIsInstance(i.TagName, str)
            self.assertIsInstance(i.Status, str)
            if i.Value:
                self.assertIsInstance(
                    i.Value,
                    (
                        bool,
                        int,
                        str,
                        list[str],
                        float,
                        datetime,
                        list[Tag],
                        LGXDevice,
                        list[LGXDevice],
                    ),
                )

    def test_get_plc_time(self):
        payload = {"raw": False}
        response = self.pylogix._get_plc_time(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, (float, datetime))

    def test_set_plc_time(self):
        response = self.pylogix._set_plc_time()
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, (float, datetime))

    def test_get_tag_list(self):
        payload = {"all_tags": True}
        response = self.pylogix._get_tag_list(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, list)
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, Tag)

    def test_get_program_tag_list(self):
        payload = {"program_name": "some-program"}
        response = self.pylogix._get_program_tag_list(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, list)
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, Tag)

    def test_get_programs_list(self):
        response = self.pylogix._get_programs_list()
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, list)
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, str)
        else:
            self.assertIsInstance(response.response.Value, str)

    def test_discover(self):
        response = self.pylogix._discover()
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, list)
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, LGXDevice)
        else:
            self.assertIsInstance(response.response.Value, LGXDevice)

    def test_get_module_properties(self):
        payload = {"slot":0}
        response = self.pylogix._get_module_properties(**payload)
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, LGXDevice)
        else:
            self.assertIsInstance(response.response.Value, LGXDevice)

    def test_get_device_properties(self):
        response = self.pylogix._get_device_properties()
        self.assertIsInstance(response, ServerResponse)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, LGXDevice)
        else:
            self.assertIsInstance(response.response.Value, LGXDevice)

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

import unittest
from datetime import datetime
from flask import Flask
from webview import Window

from models import (
        ResponseDTO,
        ConnectReqDTO, ConnectResDTO,
        CloseReqDTO, CloseResDTO,
        GetConnectionSizeReqDTO, GetConnectionSizeResDTO,
        SetConnectionSizeReqDTO, SetConnectionSizeResDTO,
        ReadReqDTO, ReadResDTO,
        WriteReqDTO, WriteResDTO,
        GetPlcTimeReqDTO, GetPlcTimeResDTO,
        SetPlcTimeReqDTO, SetPlcTimeResDTO,
        GetTagListReqDTO, GetTagListResDTO,
        GetProgramTagListReqDTO, GetProgramTagListResDTO,
        GetProgramsListReqDTO, GetProgramsListResDTO,
        DiscoverReqDTO, DiscoverResDTO,
        GetModulePropertiesReqDTO, GetModulePropertiesResDTO,
        GetDevicePropertiesReqDTO, GetDevicePropertiesResDTO,
        LGXDevice, Tag
)
from server import Server
from app import App
from factory import Factory

class FactoryTests(unittest.TestCase):

    def setUp(self) -> None:
        Server.application = None

        return super().setUp()

    def test_create_app(self):
        application = Factory.create_app(simulate=True)
        self.assertIsInstance(application, App)

    def test_create_server(self):
        application = Factory.create_app(simulate=True)
        server = Factory.create_server(application)
        self.assertIsInstance(server, Flask)
        self.assertIsInstance(Server.application, App)

    def test_create_window(self):
        application = Factory.create_app(simulate=True)
        server = Factory.create_server(application=application)
        window = Factory.create_window(server=server, window_name="some-name")
        self.assertIsInstance(Server.application, Window)

    def tearDown(self) -> None:
        return super().tearDown()

class AppTests(unittest.TestCase):

    def setUp(self) -> None:
        self.app = Factory.create_app(simulate=True)

        # the following tests app.connection()
        payload = ConnectReqDTO(
            ip_address="192.168.1.196",
            slot=0,
            timeout=5,
            Micro800=False
        )
        response = self.app.connect(req=payload)
        self.assertIsInstance(response, ConnectResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

        return super().setUp()

    def test_close(self):
        payload = CloseReqDTO()
        response = self.app.close(req=payload)
        self.assertIsInstance(response, CloseResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_get_connection_size(self):
        payload = GetConnectionSizeReqDTO()
        response = self.app.get_connection_size(req=payload)
        self.assertIsInstance(response, GetConnectionSizeResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_set_connection_size(self):
        payload = SetConnectionSizeReqDTO(
            connection_size=508
        )
        response = self.app.set_connection_size(req=payload)
        self.assertIsInstance(response, SetConnectionSizeResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")

    def test_read(self):
        payload = ReadReqDTO(
            tag="sometag"
        )
        response = self.app.read(req=payload)
        self.assertIsInstance(response, ReadResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertIsInstance(response.responses, list)
        for i in response.responses:
            self.assertIsInstance(i, ResponseDTO)
            self.assertIsInstance(i.tag, str)
            self.assertIsInstance(i.status, str)
            self.assertIsInstance(i.error, bool)
            if i.value:
                self.assertIsInstance(i.value, (bool, int, str, list[str], float, datetime, list[Tag], LGXDevice, list[LGXDevice]))
                self.assertEqual(i.status, "200 OK")
                self.assertEqual(i.error, False)

    def test_write(self):
        payload = WriteReqDTO(
            tag="sometag",
            value=619
        )
        response = self.app.write(req=payload)
        self.assertIsInstance(response, WriteResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertIsInstance(response.responses, list)
        for i in response.responses:
            self.assertIsInstance(i, ResponseDTO)
            self.assertIsInstance(i.tag, str)
            self.assertIsInstance(i.status, str)
            self.assertIsInstance(i.error, bool)
            if i.value:
                self.assertIsInstance(i.value, (bool, int, str, list[str], float, datetime, list[Tag], LGXDevice, list[LGXDevice]))
                self.assertEqual(i.status, "200 OK")
                self.assertEqual(i.error, False)

    def test_get_plc_time(self):
        payload = GetPlcTimeReqDTO(
            raw=False
        )
        response = self.app.get_plc_time(req=payload)
        self.assertIsInstance(response, GetPlcTimeResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, (float, datetime))

    def test_set_plc_time(self):
        payload = SetPlcTimeReqDTO()
        response = self.app.set_plc_time(req=payload)
        self.assertIsInstance(response, SetPlcTimeResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, (float, datetime))

    def test_get_tag_list(self):
        payload = GetTagListReqDTO(
            all_tags=True
        )
        response = self.app.get_tag_list(req=payload)
        self.assertIsInstance(response, GetTagListResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, list)
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, Tag)

    def test_get_program_tag_list(self):
        payload = GetProgramTagListReqDTO(
            program_name="someprogram"
        )
        response = self.app.get_program_tag_list(req=payload)
        self.assertIsInstance(response, GetProgramTagListResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, list)
        if isinstance(response.response.Value, list):
            for i in response.response.Value:
                self.assertIsInstance(i, Tag)

    def test_get_programs_list(self):
        payload = GetProgramsListReqDTO()
        response = self.app.get_programs_list(req=payload)
        self.assertIsInstance(response, GetProgramsListResDTO)
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
        payload = DiscoverReqDTO()
        response = self.app.discover(req=payload)
        self.assertIsInstance(response, DiscoverResDTO)
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
        payload = GetModulePropertiesReqDTO(
            slot=0
        )
        response = self.app.get_module_properties(req=payload)
        self.assertIsInstance(response, GetModulePropertiesResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, LGXDevice)

    def test_get_device_properties(self):
        payload = GetDevicePropertiesReqDTO()
        response = self.app.get_device_properties(req=payload)
        self.assertIsInstance(response, GetDevicePropertiesResDTO)
        self.assertEqual(response.error, False)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.response.Status, "Success")
        self.assertIsInstance(response.response.Value, LGXDevice)

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()

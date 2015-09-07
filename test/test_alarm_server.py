from unittest.mock import MagicMock

__author__ = 'milonaki'

import unittest
import sys
sys.path.insert(0, '/home/milonaki/Documents/alarm/alarm_server')
sys.path.insert(0, '/home/milonaki/Documents/alarm/alarm_client')


from alarm_server import AlarmServer
from alarm_client import AlarmClient


from unittest import mock



class MyTestCase(unittest.TestCase):
    def test_init_alarm_server(self):
        server = AlarmServer()
        self.assertNotEqual(server, None)
        self.assertNotEqual(server.notification_manager, None)
        self.assertNotEqual(server.sensor_manager, None)
        
    def test_init_alarm_client(self):
        client = AlarmClient()
        self.assertNotEqual(client, None)
        self.assertNotEqual(client.indicator, None)
        self.assertNotEqual(client.keypad, None)
        self.assertNotEqual(client.server_interface, None)

    def test_alarm_client_arm_contacts_command(self):
        client = AlarmClient()
        client.keypad.get_command_code = mock.MagicMock(return_value='1#')
        client.command_dictionary['1#'] = mock.MagicMock()
        client.server_interface.arm_contacts = mock.MagicMock(return_value=True)
        client.start()
        client.keypad.get_command_code.assert_called_once_with()
        client.command_dictionary['1#'].assert_called_once_with()





        

        
if __name__ == '__main__':
    unittest.main()

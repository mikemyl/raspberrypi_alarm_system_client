from indicator import Indicator
from keypad import Keypad
from server_interface import ServerInterface

class AlarmClient:
    
    def __init__(self):
        self.keypad = Keypad()
        self.indicator = Indicator()
        self.server_interface = ServerInterface()
        self.command_code = None
        self.command_dictionary = {'1#': self.server_interface.arm_contacts, 
                                   '2':  self.server_interface.arm_all_sensors
        }


    def start(self):
        while not self.command_code in self.command_dictionary:
            print('a')
            self.command_code = self.keypad.get_command_code()
        print(self.command_code)
        print(self.command_dictionary[self.command_code])
        self.command_dictionary[self.command_code]()
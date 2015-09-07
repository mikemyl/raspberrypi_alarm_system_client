'''
Created on Sep 5, 2015

@author: milonaki
'''
from notification_manager import NotificationManager
from sensor_manager import SensorManager

class AlarmServer(object):
    '''
    classdocs
    '''
    pass


    def register_callbacks(self):
        print('xai') 
        pass
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.notification_manager = NotificationManager()
        self.sensor_manager = SensorManager()
        self.register_callbacks()

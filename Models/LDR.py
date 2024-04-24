from Models.Sensor import *
from Models.Analogic import *

class LDRSensor(Sensor, Analogic):

    __value: float

    def __init__(self): 
        Sensor.__init__(self, "LDR")
        Analogic.__init__(self, 0)
        self.__value = 0

    def get_value(self) -> float: return self.__value
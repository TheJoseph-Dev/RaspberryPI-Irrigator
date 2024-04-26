from Models.Sensor import *
from Models.Analogic import *

class LDRSensor(Sensor, Analogic):

    __value: float

    def __init__(self, mcp_ch: int = 0): 
        Sensor.__init__(self, "LDR")
        Analogic.__init__(self, mcp_ch)
        self.__value = 0

    #def update(self): self.__value = self..get_value()
    def get_sensor_value(self) -> float: 
        self.__value = self.get_value()
        return self.__value
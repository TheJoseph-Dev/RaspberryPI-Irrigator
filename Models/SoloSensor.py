from Models.Sensor import Sensor
from Models.Analogic import Analogic

class SoloSensor(Sensor, Analogic):

    __value: float

    def __init__(self, mcp_ch: int):
        Sensor.__init__(self, "Solo")
        Analogic.__init__(self, mcp_ch)
        self.__value = 0

    def get_sensor_value(self) -> float: 
        self.__value = 1-self.get_value()
        return self.__value
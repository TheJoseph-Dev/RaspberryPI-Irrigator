from Models.Sensor import Sensor
from Models.Analogic import Analogic

class SoloSensor(Sensor, Analogic):

    def __init__(self):
        Sensor.__init__(self, "Solo")
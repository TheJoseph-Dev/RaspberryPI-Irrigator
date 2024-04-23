from Models.Sensor import *
from Models.Analogic import *

class LDRSensor(Sensor, Analogic):
    def __init__(self): 
        Sensor.__init__(self, "LDR")
        Analogic.__init__(self, 0)
from Models.Component import *

class Sensor(Component):
    name: str
    __status: int
    def __init__(self, name):
        Component.__init__(self)
        self.__status = 0
        self.name = name
        self.print()
    
    def get_status(self) -> int: return self.__status

    def print(self): print(f"{self.name} Sensor - Status: {self.__status}")
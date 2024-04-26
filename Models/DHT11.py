from Models.Sensor import *

import board
import adafruit_dht

class DHT11Sensor(Sensor):

    __temperature: float
    __humidity: float

    # Initial the dht device, with data pin connected to:
    __dhtDevice = adafruit_dht.DHT11(board.D27)

    def __init__(self):
        Sensor.__init__(self, "DHT11")
        self.__temperature = 0
        self.__humidity = 0
        #self.__dht11 = DHT11()        

    def get_temperature(self) -> float:
        if not self.is_active():
            print(f"Tried to get - temperature - from Sensor: {self.name} while off")
            return None
        try:
            self.__temperature = self.__dhtDevice.temperature
            return self.__temperature
        except Exception as error: print(f"{error}")

    def get_humidity(self) -> float:
        if not self.is_active():
            print(f"Tried to get - humidity - from Sensor: {self.name} while off")
            return None
        try:
            self.__humidity = self.__dhtDevice.humidity
            return self.__humidity
        except Exception as error: print(f"{error}")

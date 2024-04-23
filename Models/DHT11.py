from gpiozero import LED
import time
import RPi.GPIO
import math
from Models.Sensor import *
'''
DHT11_PIN = 18

import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)

timer = 0
last_humidity = 0
last_temp = 0

temp_list = []
hum_list = []

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        temp_list.append(temperature_c)
        hum_list.append(humidity)

        temp_avrg = sum(temp_list)/len(temp_list)
        hum_avrg = sum(hum_list)/len(hum_list) 

        last_humidity = humidity
        last_temp = temperature_c
        timer += 0.01
        
        print(
            "\nAvarage Temp: {:.1f} °C\nAvarage Humidity: {:.1f}%\nTemp: {:.1f} C   Humidity: {}% ".format(
                temp_avrg, hum_avrg, temperature_c, humidity
            )
        )
        

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)'''

import board
import adafruit_dht

class DHT11Sensor(Sensor):

    __temperature: float
    __humidity: float

    #DHT11_PIN = 18
    # Initial the dht device, with data pin connected to:
    __dhtDevice = adafruit_dht.DHT11(board.D18)

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

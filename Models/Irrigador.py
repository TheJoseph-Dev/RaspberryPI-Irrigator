from Models.Sensor import *
from Models.DHT11 import *
from Models.LDR import *
from Models.Fotossintetizador import *
from Models.Bomba import *

class Irrigador():

    __is_active: bool
    led: LED
    ldr: LDRSensor
    dht11: DHT11Sensor
    solo_sensor: SoloSensor
    fotossintetizador: Fotossintetizador
    bomba: Bomba

    def __init__(self):
        self.__is_active = False
        self.led = LED(Color.BLUE)
        self.ldr = LDRSensor()
        self.dht11 = DHT11Sensor()
        self.solo_sensor = SoloSensor()
        self.fotossintetizador = Fotossintetizador()
        self.bomba = Bomba()

    def run(self):
        self.start()
        self.update()

    def start(self):
        self.__is_active = True
        self.ldr.on()
        self.dht11.on()
        self.solo_sensor.on()
        self.bomba.on()

    def update(self):
        while self.__is_active:
            temperature = self.dht11.get_temperature()
            humidity = self.dht11.get_humidity()

    def stop(self): self.__is_active = False

    def print_name(): print("Irrigador")
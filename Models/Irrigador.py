from Models.Sensor import *
from Models.DHT11 import *
from Models.LDR import *
from Models.SoloSensor import *
from Models.Fotossintetizador import *
from Models.Bomba import *
from Models.PWM import *
from time import sleep


class Irrigador():

    __is_active: bool
    __SLEEP_TIME: float = 1.5
    led: LED
    ldr: LDRSensor
    dht11: DHT11Sensor
    solo_sensor: SoloSensor
    fotossintetizador: Fotossintetizador
    bomba: Bomba
    pwm: PWM

    def __init__(self):
        self.__is_active = False
        self.ldr = LDRSensor(0)
        self.dht11 = DHT11Sensor(board.D27)
        self.solo_sensor = SoloSensor(1)
        #self.fotossintetizador = Fotossintetizador()
        self.bomba = Bomba(19)
        self.pwm = PWM(21)

    def run(self):
        self.start()
        self.update()

    def start(self):
        self.__is_active = True
        self.ldr.on()
        self.pwm.on()
        self.dht11.on()
        self.solo_sensor.on()
        self.bomba.on()
        print("\n=====================\n")

        #with open("Data0305.txt", "w") as d_file:
        #        d_file.write("temperature humidity light_intensity\n")

    def update(self):
        while self.__is_active:
            temperature = self.dht11.get_temperature()
            humidity = self.dht11.get_humidity()
            lInt = self.ldr.get_sensor_value()
            ss_value = self.solo_sensor.get_sensor_value()
            self.pwm.set_value(100*(1-lInt))
            
            if ss_value < 0.45: self.bomba.on()
            else: self.bomba.off()
            self.bomba.update()

            print(f"\nTempertaure: {temperature}°C \nHumidity: {humidity}%")
            print(f"Light Intensity: {lInt}")
            print(f"Solo Sensor: {ss_value}")
            print(f"Bomba active: {self.bomba.is_active()}")

            sleep(self.__SLEEP_TIME)
            if temperature == None or humidity == None: continue
            #with open("Data0305.txt", "a") as d_file:
            #    d_file.write(f"{temperature} {humidity} {round(lInt*1000)/10}\n")

    def stop(self): self.__is_active = False

    def print_name(): print("Irrigador")
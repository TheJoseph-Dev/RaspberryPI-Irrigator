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
    #ledpwm: LEDPWM
    ldr: LDRSensor
    dht11: DHT11Sensor
    solo_sensor: SoloSensor
    fotossintetizador: Fotossintetizador
    bomba: Bomba
    pwm: PWM

    def __init__(self):
        self.__is_active = False
        self.led = LED(Color.BLUE)
        self.ldr = LDRSensor(0)
        self.dht11 = DHT11Sensor()
        self.solo_sensor = SoloSensor()
        self.fotossintetizador = Fotossintetizador()
        self.bomba = Bomba()
        self.pwm = PWM(21)

    def run(self):
        self.start()
        self.update()

    def start(self):
        self.__is_active = True
        self.ldr.on()
        self.led.on()
        self.pwm.on()
        self.dht11.on()
        self.solo_sensor.on()
        self.bomba.on()
        print("\n=====================\n")

        with open("Data2604.txt", "w") as d_file:
                d_file.write("temperature humidity light_intensity\n")

    def update(self):
        while self.__is_active:
            temperature = self.dht11.get_temperature()
            humidity = self.dht11.get_humidity()
            #self.ledpwm.update()
            lInt = self.ldr.get_sensor_value()
            self.pwm.set_value(100*(1-lInt))

            print(f"\nTempertaure: {temperature}°C \nHumidity: {humidity}%")
            print(f"Light Intensity: {lInt}")
            
            sleep(self.__SLEEP_TIME)
            if temperature == None or humidity == None: continue
            with open("Data2604.txt", "a") as d_file:
                d_file.write(f"{temperature} {humidity} {round(lInt*1000)/10}\n")

    def stop(self): self.__is_active = False

    def print_name(): print("Irrigador")
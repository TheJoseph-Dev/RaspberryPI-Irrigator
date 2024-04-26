from Models.Component import *
#from gpiozero import LED, Button
import RPi.GPIO
import math

class PWM(Component):
    
    pwm: RPi.GPIO.PWM

    def __init__(self, pin: int):
        Component.__init__(self)
        RPi.GPIO.setup(pin,RPi.GPIO.OUT)
        self.pwm = RPi.GPIO.PWM(pin, 100)
        self.pwm.start(100)

    def set_value(self, value:int):
        self.pwm.ChangeDutyCycle(value)
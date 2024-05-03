from Models.Component import *
from gpiozero import LED as GP_LED

# Water Pump
class Bomba(Component):

    __signal: GP_LED

    def __init__(self, pin: int):
        Component.__init__(self)
        self.__signal = GP_LED(pin)
        #self.__signal.off()

    def update(self):
        if self.is_active(): self.__signal.on()
        else: self.__signal.off()
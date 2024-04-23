from Models.Component import *

from enum import Enum
 
# Color binds to PINs
class Color(Enum):
    RED = 20
    GREEN = 21
    BLUE = 22

class LED(Component):

    #LED_PWM: LEDPWM
    color: Color

    def __init__(self, color: Color):
        Component.__init__(self)
        
        #self.LED_PWM = LEDPWM(color)
        self.color = color

    def set_color(self, color: Color):
        #self.LED_PWM = LEDPWM(color)
        self.color = color
from Models.Component import *
from gpiozero import PWMLED
from gpiozero import LED as GP_LED

from enum import Enum
 
# Color binds to PINs
class Color(Enum):
    RED = 16
    GREEN = 20
    BLUE = 21

class LED(Component):

    LED_PWM: GP_LED
    color: Color

    def __init__(self, color: Color):
        Component.__init__(self)
        
        self.LED_PWM = GP_LED(color.value)
        self.color = color

    def update(self):
        if self.is_active(): self.LED_PWM.on()
        else: self.LED_PWM.off()

    def set_color(self, color: Color):
        self.LED_PWM = GP_LED(color.value)
        self.color = color
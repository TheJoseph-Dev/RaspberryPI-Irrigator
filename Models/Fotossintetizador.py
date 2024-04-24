from Models.LED import *

class Fotossintetizador():

    __led: LED

    def __init__(self):
        print(f"G_LED:")

        self.__led = LED(Color.RED)

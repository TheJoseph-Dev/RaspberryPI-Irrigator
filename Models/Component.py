class Component():
    __is_active = False
    
    def __init__(self): pass

    def on(self): self.__is_active = True
    def off(self): self.__is_active = False
    def toggle(self): self.__is_active = not self.__is_active

    def is_active(self) -> bool: return self.__is_active   
class Length(object):
    def __init__(self):
        self.__inches = 0
        self.__feet = 0
        self.__yards = 0
        self.__links = 0
        self.__miles = 0

    @property
    def inches(self):
        return self.__inches

    @inches.setter
    def inches(self, inches):
        self.__inches = inches


class Conversions(object):
    def __init__(self):
        self.__conversion = 0
    @property
    def conversion(self):
        return self.__conversion

    @conversion.setter
    def conversion(self, conversion):
        pass

    def inches_feet(self, inches):
        self.__conversion = inches / 12
        return self.conversion



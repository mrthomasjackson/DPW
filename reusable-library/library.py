class MetricUnitConverter(object):
    def __init__(self):
        self.__inches = 0
        self.__feet = 0
        self.__centimeters = 0
        self.__pounds = 0
        self.__kilograms = 0

    def height_converter(self, feet, inches):
        inch1 = int(feet) * 12
        inch2 = int(inches)
        total_inches = inch1 + inch2
        centimeters = total_inches * 2.54
        meters = centimeters * 0.01
        return meters

    def weight_converter(self, pounds):
        kg = int(pounds) * 0.453592
        return kg

    def inches_only(self, feet, inches):
        inch1 = int(feet) * 12
        inch2 = int(inches)
        total_inches = inch1 + inch2
        return total_inches

    def metric_bmi_calculator(self, weight, height):
        bmi = ((float(weight)) / (float(height) ** 2))
        return bmi

    def english_bmi_calculator(self, weight, height):
        bmi = ((float(weight)) / (float(height) ** 2)) * 703
        return bmi
class NameHandler(object):
    def __init__(self):
        self.__name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



class DataHolder(object):
    def __init__(self):
        self.__name = ''
        self.__inches = 0
        self.__feet = 0
        self.__total_inches = 0
        self.__centimeters = 0
        self.__meters = 0
        self.__pounds = 0
        self.__kilograms = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def inches(self):
        return self.__inches

    @inches.setter
    def inches(self, inches):
        self.__inches = inches

    @property
    def feet(self):
        return self.__feet

    @feet.setter
    def feet(self, feet):
        self.__feet = feet

    @property
    def total_inches(self):
        return self.__total_inches

    @total_inches.setter
    def total_inches(self, inches):
        self.__total_inches = inches

    @property
    def centimeters(self):
        return self.__centimeters

    @centimeters.setter
    def centimeters(self, centimeters):
        self.__centimeters = centimeters

    @property
    def meters(self):
        return self.__meters

    @meters.setter
    def meters(self, meters):
        self.__meters = meters

    @property
    def pounds(self):
        return self.__pounds

    @pounds.setter
    def pounds(self, pounds):
        self.__pounds = pounds

    @property
    def kilograms(self):
        return self.__kilograms

    @kilograms.setter
    def kilograms(self, kilograms):
        self.__kilograms = kilograms

class MetricUnitConverter(object):
    def __init__(self):
        pass

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


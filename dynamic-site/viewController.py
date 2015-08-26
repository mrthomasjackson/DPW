class ViewController(object):
    def __init__(self):
        self.__distance_view = False
        self.__weight_view = False
        self.__volume_view = False
        self.__temperature_view = False
        self.__speed_view = False

    @property
    def distance_view(self):
        return self.__distance_view

    @distance_view.setter
    def distance_view(self, x):
        print "View is " + x
        if x == 'distance_view':
            self.__distance_view = True
        else:
            self.__distance_view = False

    @property
    def weight_view(self):
        return self.__weight_view

    @weight_view.setter
    def weight_view(self, x):
        print "View is " + x
        if x == 'weight_view':
            self.__weight_view = True
        else:
            self.__weight_view = False

    @property
    def volume_view(self):
        return self.__volume_view

    @volume_view.setter
    def volume_view(self, x):
        print "View is " + x
        if x == 'volume_view':
            self.__volume_view = True
        else:
            self.__volume_view = False

    @property
    def temperature_view(self):
        return self.__temperature_view

    @temperature_view.setter
    def temperature_view(self, x):
        print "View is " + x
        if x == 'temperature_view':
            self.__temperature_view = True
        else:
            self.__temperature_view = False

    @property
    def speed_view(self):
        return self.__speed_view

    @speed_view.setter
    def speed_view(self, x):
        print "View is " + x
        if x == 'speed_view':
            self.speed_view = True
        else:
            self.speed_view = False


class Data(object):
    def __init__(self):
        self.__country = ''
        self.__capital = ''
        self.__currency = ''
        self.__gdp = ''
        self.__population = ''

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, capital):
        self.__capital = capital

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    @property
    def gdp(self):
        return self.__gdp

    @gdp.setter
    def gdp(self, gdp):
        self.__gdp = gdp

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population



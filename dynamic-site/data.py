# create parent class to hold data
class Data(object):
    def __init__(self):
        self._country = ''
        self._capital = ''
        self._currency = ''
        self._gdp = ''
        self._population = ''

    # create getter and setter for data attribute
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    # create getter and setter for data attribute
    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, capital):
        self._capital = capital

    # create getter and setter for data attribute
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    # create getter and setter for data attribute
    @property
    def gdp(self):
        return self._gdp

    @gdp.setter
    def gdp(self, gdp):
        self._gdp = gdp

    # create getter and setter for data attribute
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population


# create classes to hold data for particular countries
class China(Data):
    def __init__(self):
        super(China, self).__init__()
        self._country = 'China'
        self._capital = 'Beijing'
        self._currency = 'Renminbi'
        self._gdp = '9.24 Trillion USD'
        self._population = '1.34 Billion'


class India(Data):
    def __init__(self):
        super(India, self).__init__()
        self._country = 'India'
        self._capital = 'New Delhi'
        self._currency = 'Rupee'
        self._gdp = '1.88 Trillion USD'
        self._population = '1.25 Billion'


class UnitedStates(Data):
    def __init__(self):
        super(UnitedStates, self).__init__()
        self._country = 'United States'
        self._capital = 'Washington DC'
        self._currency = 'Dollar'
        self._gdp = '16.77 Trillion USD'
        self._population = '318.9 Million'


class Indonesia(Data):
    def __init__(self):
        super(Indonesia, self).__init__()
        self._country = 'Indonesia'
        self._capital = 'Jakarta'
        self._currency = 'Rupiah'
        self._gdp = '868.3 Billion USD'
        self._population = '249.9 Million'


class Brazil(Data):
    def __init__(self):
        super(Brazil, self).__init__()
        self._country = 'Brazil'
        self._capital = 'Brazilia'
        self._currency = 'Real'
        self._gdp = '2.25 Trillion USD'
        self._population = '200.4 Million'





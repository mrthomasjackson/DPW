class Data(object):
    def __init__(self):
        self._country = ''
        self._capital = ''
        self._currency = ''
        self._gdp = ''
        self._population = ''

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, capital):
        self._capital = capital

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def gdp(self):
        return self._gdp

    @gdp.setter
    def gdp(self, gdp):
        self._gdp = gdp

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population


class China(Data):
    def __init__(self):
        super(China, self).__init__()
        self.country = 'China'
        self.capital = 'Beijing'
        self.currency = 'Renminbi'
        self.gdp = '9.24 Trillion USD'
        self.population = '1.34 Billion'


class India(Data):
    def __init__(self):
        super(India, self).__init__()
        self.country = 'India'
        self.capital = 'New Delhi'
        self.currency = 'Rupee'
        self.gdp = '1.88 Trillion USD'
        self.population = '1.25 Billion'


class UnitedStates(Data):
    def __init__(self):
        super(UnitedStates, self).__init__()
        self.country = 'United States'
        self.capital = 'Washington DC'
        self.currency = 'Dollar'
        self.gdp = '16.77 Trillion USD'
        self.population = '318.9 Million'


class Indonesia(Data):
    def __init__(self):
        super(Indonesia, self).__init__()
        self.country = 'Indonesia'
        self.capital = 'Jakarta'
        self.currency = 'Rupiah'
        self.gdp = '868.3 Billion USD'
        self.population = '249.9 Million'


class Brazil(Data):
    def __init__(self):
        super(Brazil, self).__init__()
        self.country = 'Brazil'
        self.capital = 'Brazilia'
        self.currency = 'Real'
        self.gdp = '2.25 Trillion USD'
        self.population = '200.4 Million'





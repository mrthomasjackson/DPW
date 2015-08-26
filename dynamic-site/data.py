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
        self.country = 'China'
        self.capital = 'Beijing'
        self.currency = 'Renminbi'
        self.gdp = '9.24 Trillion USD'
        self.population = '1.34 Billion'


class UnitedStates(Data):
    def __init__(self):
        super(UnitedStates, self).__init__()
        self.country = 'China'
        self.capital = 'Beijing'
        self.currency = 'Renminbi'
        self.gdp = '9.24 Trillion USD'
        self.population = '1.34 Billion'


class Indonesia(Data):
    def __init__(self):
        super(Indonesia, self).__init__()
        self.country = 'China'
        self.capital = 'Beijing'
        self.currency = 'Renminbi'
        self.gdp = '9.24 Trillion USD'
        self.population = '1.34 Billion'


class Brazil(Data):
    def __init__(self):
        super(Brazil, self).__init__()
        self.country = 'China'
        self.capital = 'Beijing'
        self.currency = 'Renminbi'
        self.gdp = '9.24 Trillion USD'
        self.population = '1.34 Billion'





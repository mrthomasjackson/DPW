class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
                '''
        self._body = ''
        self._close = '''
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>
                '''

    def print_out(self):
        return self._open + self._body + self._close


class MainPage(Page):
    def __init__(self):
        super(MainPage, self).__init__()
        self._body = '''
        <div class="container">
            <img src="home-img.jpg" class="img-responsive" alt="Responsive image">
            <ul class="nav nav-pills nav-stacked">
                <li role="presentation"><a href="?country=China&capital=Beijing&currency=Renminbi&gdp=9.24%20trillion&population=1.34%20billion" class="button button-default">China</a></li>
                <li role="presentation"><a href="?country=India&capital=New%20Delhi&currency=Rupee&gdp=1.88%20trillion&population=1.25%20billion" class="button button-default">India</a></li>
                <li role="presentation"><a href="?country=United%20States&capital=Washington%20DC&currency=Dollar&gdp=16.77%20trillion&population=318.9%20million" class="button button-default">United States</a></li>
                <li role="presentation"><a href="?country=Indonesia&capital=Jakarta&currency=Rupiah&gdp=868.3%20billion&population=249.9%20million" class="button button-default">Indonesia</a></li>
                <li role="presentation"><a href="?country=Brazil&capital=Brasilia&currency=Real&gdp=2.25%20trillion&population=200.4%20million" class="button button-default">China</a></li>
            </ul>
        </div>
        '''

    def print_out(self):
        return self._open + self._body + self._close

class FinalView(Page):
    def __init__(self):
        super(FinalView, self).__init__()
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

        self._body = '''
        <div class="container">
        <div class='jumbotron'>
            <h1>{self.country}</h1>
        </div>
        <div class="list-group">
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Captial:</h2>
                <p class="list-group-item-text">{self.capital}</p>
            </div>
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Currency:</h2>
                <p class="list-group-item-text">{self.currency}</p>
            </div>
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Gross Domestic Product:</h2>
                <p class="list-group-item-text">{self.gdp}</p>
            </div>
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Population:</h2>
                <p class="list-group-item-text">{self.population}</p>
            </div>
        </div>
        <a href="/">Take Me Back</a>
        </div>
        '''

    def print_out(self):
        page = self._open + self._body + self._close
        page = page.format(**locals())
        return page

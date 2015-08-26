# create class to hold basic HTML backbone
class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/styles.css" rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Top 5 Countries By Population</a>
            </div><!-- /.container-fluid -->
        </nav>
                '''
        self._body = ''
        self._close = '''
        <div class="row">
            <div class="col-xs-12">
                <div class="jumbotron">
                    <h2>Photo Credit</h2>
                    <p>Thank you to <a href="https://www.flickr.com/photos/teegardin/6093690339">Ken Teegardin</a><p>
                </div>
            </div>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>
                '''
    # function to print out HTML to browser
    def print_out(self):
        return self._open + self._body + self._close


# sub-class of Page class to hold default view
class MainPage(Page):
    def __init__(self):
        super(MainPage, self).__init__()
        self._body = '''
        <div class="row my-row">
            <div class="col-xs-12 col-md-offset-2 col-md-4 col-lg-3">
            <div class="my-container list-group">
                <a class="btn btn-lg btn-default list-group-item" href="?country=China" class="button button-default">China</a>
                <a class="btn btn-lg btn-default list-group-item" href="?country=India" class="button button-default">India</a>
                <a class="btn btn-lg btn-default list-group-item" href="?country=UnitedStates" class="button button-default">United States</a>
                <a class="btn btn-lg btn-default list-group-item" href="?country=Indonesia" class="button button-default">Indonesia</a>
                <a class="btn btn-lg btn-default list-group-item" href="?country=Brazil" class="button button-default">Brazil</a>
            </div>
            </div>
        </div>
        '''

    # polymorphic class of print out
    def print_out(self):
        return self._open + self._body + self._close


# detailed view is a subclass of Page class
class FinalView(Page):
    def __init__(self):
        super(FinalView, self).__init__()
        self.__country = ''
        self.__capital = ''
        self.__currency = ''
        self.__gdp = ''
        self.__population = ''

    # create getters and setters for data attributes above
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
                <p class="list-group-item-text text-danger ">{self.capital}</p>
            </div>
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Currency:</h2>
                <p class="list-group-item-text text-danger ">{self.currency}</p>
            </div>
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Gross Domestic Product:</h2>
                <p class="list-group-item-text text-danger ">{self.gdp}</p>
            </div>
            <div class='list-group-item'>
                <h2 class="list-group-item-heading">Population:</h2>
                <p class="list-group-item-text text-danger ">{self.population}</p>
            </div>
        </div>
        <a class="home" href="/">Take Me Back</a>
        </div>
        '''

    # polymorphic class to override Page.print_out
    def print_out(self):
        page = self._open + self._body + self._close
        page = page.format(**locals())
        return page

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
        <a href="?country=China&captial=Beijing&currency=Renminbi&gdp=9.24%20trillion&population=1.34%20billion" class="button button-default">China</a>
        <a href="?country=India&captial=New%20Delhi&currency=Rupee&gdp=1.88%20trillion&population=1.25%20billion" class="button button-default">India</a>
        <a href="?country=United%20States&captial=Washington%20DC&currency=Dollar&gdp=16.77%20trillion&population=318.9%20million" class="button button-default">United States</a>
        <a href="?country=Indonesia&captial=Jakarta&currency=Rupiah&gdp=868.3%20billion&population=249.9%20million" class="button button-default">Indonesia</a>
        <a href="?country=Brazil&captial=Brasilia&currency=Real&gdp=2.25%20trillion&population=200.4%20million" class="button button-default">China</a>
        '''

    def print_out(self):
        return self._open + self._body + self._close




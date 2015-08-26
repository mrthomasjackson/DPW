class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
                '''
        self._body = ''
        self._close = '''
    </body>
</html>
                '''

    def print_out(self):
        return self._open + self._body + self._close

class MainPage(Page):
    def __init__(self):
        super(MainPage, self).__init__()
        self._body = '''
        <form
        '''

class DistancePage(Page):
    def __init__(self):
        super(DistancePage, self).__init__()
        self._open_form = '<form method="GET">'
        self._close_form = '</form>'
        self.__form_arr = []
        self._form_inputs = ''

    @property
    def form_arr(self):
        pass

    @form_arr.setter
    def form_arr(self, arr):
        pass




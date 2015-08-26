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

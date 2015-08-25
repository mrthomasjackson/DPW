import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
        '''
        self._body = "my body"
        self._close = '''
    </body>
</html>
        '''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

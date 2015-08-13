'''
Thomas Jackson
08/12/2015
DPW
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = PageView()
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(p.page_head + user + email + p.page_close)
        else:
            self.response.write(p.page_head + p.page_body + p.page_close)
class PageView(object):
    def __init__(self):
        self.page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <link href="/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        self.page_body = '''
        <form method="GET" action="">
            <label for="user">User: </label><input type="text" name="user" />
            <label for="email">Email: </label><input type="text" name="email" />
            <input type="submit" value="submit" />
        </form>
        '''

        self.page_close = '''
    </body>
</html>
        '''
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

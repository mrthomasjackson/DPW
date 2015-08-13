'''
Thomas Jackson
08/12/2015
DPW
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def print_html(self):
        if self.request.POST:
            user = self.request.POST['user']
            email = self.request.POST['email']
            self.response.write(View.page_head + user + email + self.page_body + self.page_close)
        else:
            self.response.write(self.page_head + self.page_body + self.page_close)

class View(object):
    page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''
    page_body = '''<form method="GET" action="">
            <label for="user">User: </label><input type="text" name="user" />
            <label for="email">Email: </label><input type="text" name="email" />
            <input type="submit" value="submit" />
            </form>'''
    page_close = '''
    </body>
</html>
        '''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

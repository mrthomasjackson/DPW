'''
Thomas Jackson
08/12/2015
DPW
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''
        page_body = '''<form method="GET" action="">
            <label for="user">User: </label><input type="text" name="user" />
            <label for="email">Email: </label><input type="text" name="email" />
            <input type="submit" value="submit" />'''

        page_close = '''
        </form>
    </body>
</html>
        '''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + " " + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)
        # self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

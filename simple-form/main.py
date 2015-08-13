'''
Thomas Jackson
08/12/2015
DPW
Simple Form
'''
import webapp2

from view import View

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = View()
        self.response.write(page.print_html())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

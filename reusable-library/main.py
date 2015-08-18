import webapp2
from pages import Page
from library import Length

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        length = Length()
        length.inches = 24
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

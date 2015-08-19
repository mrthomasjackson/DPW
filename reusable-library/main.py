import webapp2
from pages import Page
from library import Length, Conversions

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = Conversions()
        self.response.write(p.print_out())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

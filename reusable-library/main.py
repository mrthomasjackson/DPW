import webapp2
from pages import Page
from library import Length, Conversions

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        convert = Conversions()
        to_body = convert.inches_feet(12)

        p.body = str(to_body)

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

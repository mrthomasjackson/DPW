import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        if self.request.GET:
            feet = self.request.GET['name']

        else:
            self.response.write(p.print_out())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

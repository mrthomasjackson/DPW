import webapp2
from pages import *
class MainHandler(webapp2.RequestHandler):
    def get(self):
        mainPage = MainPage()
        if self.request.GET:


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

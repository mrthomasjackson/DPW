import webapp2
from pages import *
class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        mainPage = MainPage()

        if self.request.GET:

        else:
            self.response.write(mainPage.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

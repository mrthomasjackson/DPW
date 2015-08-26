import webapp2
from pages import *
from data import Data
class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_page = MainPage()
        data = Data()

        if self.request.GET:
            data.country = self.request.GET['country']
            data.capital = self.request.GET['capital']
            data.currency = self.request.GET['currency']
            data.gdp = self.request.GET['gdp']
            data.population = self.request.GET['population']
        else:
            self.response.write(main_page.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

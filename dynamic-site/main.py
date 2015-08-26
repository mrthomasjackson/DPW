import webapp2
from pages import *
from data import Data
class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_page = MainPage()
        final_view = FinalView()
        data = Data()

        if self.request.GET:
            data.country = self.request.GET['country']
            data.capital = self.request.GET['capital']
            data.currency = self.request.GET['currency']
            data.gdp = self.request.GET['gdp']
            data.population = self.request.GET['population']
            final_view.country = data.country
            final_view.capital = data.capital
            final_view.currency = data.currency
            final_view.gdp = data.gdp
            final_view.population = data.population
            self.response.write(final_view.print_out())
        else:
            self.response.write(main_page.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

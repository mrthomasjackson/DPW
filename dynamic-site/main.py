import webapp2
from pages import *
from data import *
class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_page = MainPage()
        final_view = FinalView()
        data = Data()
        china = China()
        india = India()
        usa = UnitedStates()
        indonesia = Indonesia()
        brazil = Brazil()

        if self.request.GET:
            data.country = self.request.GET['country']
            if data.country == "China":
                final_view.country = china.country
                final_view.capital = china.capital
                final_view.currency = china.currency
                final_view.gdp = china.gdp
                final_view.population = china.population
                self.response.write(final_view.print_out())
            elif data.country == "India":
                final_view.country = india.country
                final_view.capital = india.capital
                final_view.currency = india.currency
                final_view.gdp = india.gdp
                final_view.population = india.population
                self.response.write(final_view.print_out())
            elif data.country == "UnitedStates":
                final_view.country = usa.country
                final_view.capital = usa.capital
                final_view.currency = usa.currency
                final_view.gdp = usa.gdp
                final_view.population = usa.population
                self.response.write(final_view.print_out())
            elif data.country == "Indonesia":
                final_view.country = indonesia.country
                final_view.capital = indonesia.capital
                final_view.currency = indonesia.currency
                final_view.gdp = indonesia.gdp
                final_view.population = indonesia.population
                self.response.write(final_view.print_out())
            elif data.country == "Brazil":
                final_view.country = brazil.country
                final_view.capital = brazil.capital
                final_view.currency = brazil.currency
                final_view.gdp = brazil.gdp
                final_view.population = brazil.population
                self.response.write(final_view.print_out())
        else:
            self.response.write(main_page.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

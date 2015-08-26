import webapp2
from pages import *
from data import *
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # create instances of view classes
        main_page = MainPage()
        final_view = FinalView()
        # create instances of data classes
        data = Data()
        china = China()
        india = India()
        usa = UnitedStates()
        indonesia = Indonesia()
        brazil = Brazil()

        # listen for values in the URL
        if self.request.GET:
            # add key pair value to data.country attribute
            data.country = self.request.GET['country']
            # if China
            if data.country == "China":
                # load the data into the view
                final_view.country = china.country
                final_view.capital = china.capital
                final_view.currency = china.currency
                final_view.gdp = china.gdp
                final_view.population = china.population
                # write the view to the browser
                self.response.write(final_view.print_out())
            # if India
            elif data.country == "India":
                # load the data into the view
                final_view.country = india.country
                final_view.capital = india.capital
                final_view.currency = india.currency
                final_view.gdp = india.gdp
                final_view.population = india.population
                # write the view into the browser
                self.response.write(final_view.print_out())
            elif data.country == "UnitedStates":
                # load the data into the view
                final_view.country = usa.country
                final_view.capital = usa.capital
                final_view.currency = usa.currency
                final_view.gdp = usa.gdp
                final_view.population = usa.population
                # write the view into the browser
                self.response.write(final_view.print_out())
            elif data.country == "Indonesia":
                # load the data into the view
                final_view.country = indonesia.country
                final_view.capital = indonesia.capital
                final_view.currency = indonesia.currency
                final_view.gdp = indonesia.gdp
                final_view.population = indonesia.population
                # write the view into the browser
                self.response.write(final_view.print_out())
            elif data.country == "Brazil":
                # load the data into the view
                final_view.country = brazil.country
                final_view.capital = brazil.capital
                final_view.currency = brazil.currency
                final_view.gdp = brazil.gdp
                final_view.population = brazil.population
                # write the view into the browser
                self.response.write(final_view.print_out())
        else:
            self.response.write(main_page.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

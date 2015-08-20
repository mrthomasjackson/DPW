import webapp2
from pages import Page
from library import MetricUnitConverter, DataHolder

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # create instance of the view
        p = Page()
        # create instance of the converter class
        u = MetricUnitConverter()
        # create instance of the data library class
        data = DataHolder()
        # if/ else statement to determine which view to throw
        if self.request.GET:
            # form inputs are stores in the data library
            data.name = self.request.GET['name']
            data.feet = self.request.GET['feet']
            data.inches = self.request.GET['inches']
            data.pounds = self.request.GET['weight']
            # calculations are returned to the data library
            data.meters = u.height_converter(data.feet, data.inches)
            data.kilograms = u.weight_converter(data.pounds)
            # english BMI requires height to be in inches only
            data.total_inches = u.inches_only(data.feet, data.inches)
            p.english_bmi = u.english_bmi_calculator(data.pounds, data.total_inches)
            p.metric_bmi = u.metric_bmi_calculator(data.kilograms, data.meters)
            # name is stored in the data library as well
            p.name = data.name
            # Custom message is injected into the h1 tag
            p.message = "Thanks for filling out our form!"
            # generate the results view
            self.response.write(p.write_answer())
        # else statement to hold the form view (1st view)
        else:
            # generate the form view (1st view)
            self.response.write(p.write_form())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

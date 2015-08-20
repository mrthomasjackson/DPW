import webapp2
from pages import Page
from library import MetricUnitConverter, DataHolder

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        u = MetricUnitConverter()
        data = DataHolder()

        if self.request.GET:
            data.name = self.request.GET['name']
            data.feet = self.request.GET['feet']
            data.inches = self.request.GET['inches']
            data.pounds = self.request.GET['weight']
            data.meters = u.height_converter(data.feet, data.inches)
            data.kilograms = u.weight_converter(data.pounds)
            data.total_inches = u.inches_only(data.feet, data.inches)
            p.english_bmi = u.english_bmi_calculator(data.pounds, data.total_inches)
            p.metric_bmi = u.metric_bmi_calculator(data.kilograms, data.meters)
            p.name = data.name

            self.response.write(p.write_answer())


        else:
            self.response.write(p.write_form())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

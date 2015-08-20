import webapp2
from pages import Page
from library import MetricUnitConverter

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        u = MetricUnitConverter()

        if self.request.GET:
            name = self.request.GET['name']
            feet = self.request.GET['feet']
            inches = self.request.GET['inches']
            weight = self.request.GET['weight']
            meters = u.height_converter(feet, inches)
            kilograms = u.weight_converter(weight)
            only_inches = u.inches_only(feet, inches)
            p.english_bmi = u.english_bmi_calculator(weight, only_inches)
            p.metric_bmi = u.metric_bmi_calculator(kilograms, meters)
            u

            self.response.write(p.write_answer())


        else:
            self.response.write(p.write_form())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

import webapp2
from pages import Page
from library import Length, Conversions

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = Conversions()
        self.response.write(p.print_out())


        if self.request.GET:
            conversion_type = self.request.GET['conversionType']
            if conversion_type == 'length':
                self.response.write(p.print_length())
            elif conversion_type == 'area':
                self.response.write(p.print_length())
            else:
                pass

        else:
            pass





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

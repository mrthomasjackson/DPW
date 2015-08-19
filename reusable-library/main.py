import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
<<<<<<< HEAD
        if self.request.GET:
            name = self.request.GET['name']
            print name

        else:
            self.response.write(p.print_out())



=======
        convert = Conversions()
        to_body = convert.inches_feet(12)
>>>>>>> parent of 9de2ddc... Added Area and length views

        p.body = str(to_body)

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

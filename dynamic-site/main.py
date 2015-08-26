import webapp2
from pages import *
from viewController import *
class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        mainPage = MainPage()
        viewController = ViewController()





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

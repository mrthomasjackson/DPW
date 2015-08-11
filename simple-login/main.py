
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()
class Button(object):
    def __init__(self):
        print "Button Initialized"
        self.label = ""  #public attribute
        self.__size = 60  #private attribute
        self._color = "0x000000"  # protected attribute
        # self.on_roll_over("What's Up???")

    def click(self):
        print "I've Been Clicked"

    def on_roll_over(self, message):
        print "Rolled over button" + message
    def show_label(self):
        print "My Label is " + self.label + " height "

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

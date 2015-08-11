# data objects
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi"
        luke.age = "26"
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home_planet = "Alderan"

        chars = [luke, leia]
        print chars

class Character(object):
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Transcript(object):
    def __init__(self):
        self.grade1 = 0 # public attribute
        self.grade2 = 0
        self.quiz1 = 0
        self.final_exam = 0
        self.__final_grade = 0 # private attribute


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


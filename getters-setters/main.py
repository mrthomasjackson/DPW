import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = Transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_exam = 100
        t.final_grade = 99
        self.response.write("Tommy's Grade: " + str(t.final_grade))

        s = Transcript()
        s.grade1 = 45
        s.grade2 = 85
        s.quiz1 = 70
        s.quiz2 = 80
        s.final_exam = 95
        s.calc_grade()
        self.response.write("<br>Sally's Grade: " + str(s.final_grade))

class Transcript(object):
    def __init__(self):
        self.grade1 = 0 # public attribute
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0 # private attribute

    @property
    def final_grade(self):
        return self.__final_grade

    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade

    def calc_grade(self):
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


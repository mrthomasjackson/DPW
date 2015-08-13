import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Update"
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "/css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/link>
    </head>
    <body>
        """
        self.body = "Welcome to my Python Page"
        self.close = """
    </body>
</html>
    """
    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

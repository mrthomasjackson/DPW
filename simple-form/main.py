'''
Thomas Jackson
08/12/2015
DPW
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = PageView()
        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            team = self.request.GET['team']
            world = self.request.GET['world']
            comment = self.request.GET['comment']
            self.response.write(p.page_head + name + email + team + world + comment + p.page_close)
        else:
            self.response.write(p.page_head + p.page_body + p.page_close)
class PageView(object):
    def __init__(self):
        self.page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <link href="/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        self.page_body = '''
        <form class="form-horizontal" method="GET" action="">
<fieldset>

<!-- Form Name -->
<legend>Choose Your Team and World</legend>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="name">Name</label>
  <div class="col-md-4">
  <input id="name" name="name" type="text" placeholder="" class="form-control input-md">

  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="email">Email</label>
  <div class="col-md-4">
  <input id="email" name="email" type="text" placeholder="" class="form-control input-md">

  </div>
</div>

<!-- Multiple Radios -->
<div class="form-group">
  <label class="col-md-4 control-label">Select Team</label>
  <div class="col-md-4">
  <div class="radio">
    <label for="team-0">
      <input type="radio" name="team" id="team-0" value="red" checked="checked">
      Red
    </label>
	</div>
  <div class="radio">
    <label for="team-1">
      <input type="radio" name="team" id="team-1" value="blue">
      Blue
    </label>
	</div>
  </div>
</div>

<!-- Select Basic -->
<div class="form-group">
  <label class="col-md-4 control-label" for="world">Select World</label>
  <div class="col-md-4">
    <select id="world" name="world" class="form-control">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
    </select>
  </div>
</div>

<!-- Textarea -->
<div class="form-group">
  <label class="col-md-4 control-label" for="comment">Comments</label>
  <div class="col-md-4">
    <textarea class="form-control" id="comment" name="comment"></textarea>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="submit"></label>
  <div class="col-md-4">
    <button id="submit" name="submit" class="btn btn-primary">Send</button>
  </div>
</div>

</fieldset>
</form>
        '''

        self.page_close = '''
    </body>
</html>
        '''
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

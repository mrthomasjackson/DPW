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
            phone = self.request.GET['phone']
            contact_method = self.request.GET['contact_method']
            time_of_day = self.request.GET['time_of_day']
            comment = self.request.GET['comment']
            self.response.write(p.page_head + name + email + phone + contact_method + time_of_day + comment + p.page_close)
        else:
            self.response.write(p.page_head + p.page_form + p.page_close)
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
        self.page_form = '''
        <div class="container">
        <form class="form-horizontal">
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

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="phone">Phone</label>
  <div class="col-md-4">
  <input id="phone" name="phone" type="text" placeholder="" class="form-control input-md">

  </div>
</div>

<!-- Multiple Radios -->
<div class="form-group">
  <label class="col-md-4 control-label" for="contact_method">Best Way to Reach You</label>
  <div class="col-md-4">
  <div class="radio">
    <label for="contact_method-0">
      <input type="radio" name="contact_method" id="contact_method-0" value="email" checked="checked">
      Email
    </label>
	</div>
  <div class="radio">
    <label for="contact_method-1">
      <input type="radio" name="contact_method" id="contact_method-1" value="phone">
      Phone
    </label>
	</div>
  </div>
</div>

<!-- Select Basic -->
<div class="form-group">
  <label class="col-md-4 control-label" for="time_of_day">Best Time to Reach You</label>
  <div class="col-md-4">
    <select id="time_of_day" name="time_of_day" class="form-control">
      <option value="morning">Morning</option>
      <option value="evening">Evening</option>
      <option value="night">Night</option>
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
</div>
        '''

        self.page_close = '''
    </body>
</html>
        '''
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

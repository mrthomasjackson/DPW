'''
Thomas Jackson
08/12/2015
DPW
Simple Form
'''
import webapp2

# Class habdles the webpage
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # assign the PageView class to variable
        p = PageView()
        # if statement to check if form has been filled (looking for get method in URL)
        if self.request.GET:
            # assigning form elements to variables
            name = self.request.GET['name']
            email = self.request.GET['email']
            phone = self.request.GET['phone']
            contact_method = self.request.GET['contact_method']
            time_of_day = self.request.GET['time_of_day']
            comment = self.request.GET['comment']
            # write the page with the form_results variable (including its own variables)
            self.response.write(p.page_head + p.form_results % (name, email, phone, contact_method, time_of_day, comment) + p.page_close)
        # else statement to present form if form is blank
        else:
            # write page with empty form
            self.response.write(p.page_head + p.page_form + p.page_close)
# create new class to hold templates
class PageView(object):
    # initiate the class
    def __init__(self):
        # html head elements stored below
        self.page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <link href="/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css" />
    </head>
    <body style="margin-top: 25px">'''
        # html empty form stored below
        self.page_form = '''
        <div class="container">
        <form class="form-horizontal">
<fieldset>

<!-- Form Name -->
<legend>Contact Us</legend>

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
        # html form results stored below
        self.form_results = '''
    <div class="container">
        <div class="jumbotron">
            <h2>Thank You For Filling Out Our Form!</h2>
            <p>We will be in contact with you shortly. Your details are listed below.</p>
        </div>
        <div class="list-group">
            <div class="list-group-item">
                <h4 class="list-group-item-heading">Name: </h4>
                <p class="list-group-item-text"><strong>%s</strong></p>
            </div>
            <div class="list-group-item">
                <h4 class="list-group-item-heading">Email: </h4>
                <p class="list-group-item-text"><strong>%s</strong></p>
            </div>
            <div class="list-group-item">
                <h4 class="list-group-item-heading">Phone: </h4>
                <p class="list-group-item-text"><strong>%s</strong></p>
            </div>
            <div class="list-group-item">
                <h4 class="list-group-item-heading">Best Contact Method:</h4>
                <p class="list-group-item-text"><strong>%s</strong></p>
            </div>
            <div class="list-group-item">
                <h4 class="list-group-item-heading">Best Time to Reach You: </h4>
                <p class="list-group-item-text"><strong>%s</strong></p>
            </div>
            <div class="list-group-item">
                <h4 class="list-group-item-heading">Additional Comments: </h4>
                <p class="list-group-item-text"><strong>%s</strong></p>
            </div>
        </div>
    </div>
        '''
        # html page close stored below
        self.page_close = '''
    </body>
</html>
        '''
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

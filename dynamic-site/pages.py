class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
                '''
        self._body = ''
        self._close = '''
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>
                '''

    def print_out(self):
        return self._open + self._body + self._close

class MainPage(Page):
    def __init__(self):
        super(MainPage, self).__init__()
        self._body = '''
        <form class="form-horizontal">
<fieldset>

<!-- Form Name -->
<legend>Form Name</legend>

<!-- Button -->
<div class="form-group">
  <div class="col-md-4">
    <button id="distance_view" name="distance_view" class="btn btn-primary">Distance</button>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <div class="col-md-4">
    <button id="weight_view" name="weight_view" class="btn btn-primary">Weight</button>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <div class="col-md-4">
    <button id="volume_view" name="volume_view" class="btn btn-primary">Volume</button>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <div class="col-md-4">
    <button id="temperature_view" name="temperature_view" class="btn btn-primary">Temperature</button>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <div class="col-md-4">
    <button id="speed_view" name="speed_view" class="btn btn-primary">Speed</button>
  </div>
</div>

</fieldset>
</form>
        '''

    def print_out(self):
        return self._open + self._body + self._close
    

class DistancePage(Page):
    def __init__(self):
        super(DistancePage, self).__init__()
        self._open_form = '<form method="GET">'
        self._close_form = '</form>'
        self.__form_arr = []
        self._form_inputs = ''

    @property
    def form_arr(self):
        pass

    @form_arr.setter
    def form_arr(self, arr):
        pass




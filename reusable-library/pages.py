class Page(object):
    def __init__(self):
        # create private variables to store HTML dynamic content
        self.__title = "BMI Utility"
        self.__css = "/css/styles.css"
        self.__message = "Please Fill Out The Following Form: "
        self.__english_bmi = ""
        self.__metric_bmi = ""
        self.__name = ''
        # HTML head
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
    <div class='container'>
                    """
        # self.__main does not hold content. It is there in case I want expand the app easily
        self.__main = ""
        # first/ form view
        self.__form = """
        <header>
            <h1>{self.message}</h1>
        </header>
        <div>
            <form action="" method="GET">
            <label for='name'>Name</label>
            <input type='text' name='name' id='name'></input></br>

            <label for='weight'>Weight (In Pounds)</label>
            <input type='text' name='weight' id='weight'/></br>
            <span class='form-group-label'>Height</span></br>
            <select id='feet' name='feet'>
                <option value='4'>4</option>
                <option value='5'>5</option>
                <option value='6'>6</option>
                <option value='7'>7</option>
                <option value='8'>8</option>
            </select>
            <label for="feet">:Feet</label>
            <select id='inches' name='inches'>
                <option value='0'>0</option>
                <option value='1'>1</option>
                <option value='2'>2</option>
                <option value='3'>3</option>
                <option value='4'>4</option>
                <option value='5'>5</option>
                <option value='6'>6</option>
                <option value='7'>7</option>
                <option value='8'>8</option>
                <option value='9'>9</option>
                <option value='10'>10</option>
                <option value='11'>11</option>
            </select>
            <label for="inches">:Inches</label><br>
            <input style='margin-top: 25px' class="submit" type="submit" name="submit" value="Submit" />
            </form>
        </div>
        """
        # second/ results view
        self.__results_view = '''
        <header>
            <h1>{self.message}</h1>
        </header>
        <div class='message'>
            <span class='hello'>Hello {self.name},</span><br><br>
            <span class='pre-bmi'>Your Metric BMI is </span><span class='bmi'>{self.metric_bmi}</span><br>
            <span class='pre-bmi'>Your English BMI is </span><span class='bmi'>{self.english_bmi}</span></br>
            <br>
            <a href='/' class='back' title='back'>Take Me Back</a>
        </div>
        '''
        # body doesnt contain anything eiter... ready for expansion
        self.__body = ""
        self.__error = ""
        # HTML to close out the page
        self.__close = """
    </div>
    </body>
</html>
                    """
    # getter for self.__title
    @property
    def title(self):
        return self.__title

    # setter for self.__title
    @title.setter
    def title(self, title):
        self.__title = title

    # getter for self.__body
    @property
    def body(self):
        return self.__body

    # setter for self.__body
    @body.setter
    def body(self, body):
        self.__body = body

    # getter for self.__css
    @property
    def css(self):
        return self.__css

    # setter for self.__css
    @css.setter
    def css(self, css):
        self.__css = css

    # getter for self.__message
    @property
    def message(self):
        return self.__message

    # setter for self.__message
    @message.setter
    def message(self, message):
        self.__message = message

    # getter for self.__english_bmi
    @property
    def english_bmi(self):
        return self.__english_bmi

    # setter for self.__english_bmi
    @english_bmi.setter
    def english_bmi(self, value):
        self.__english_bmi = value

    # getter for self.__metric_bmi
    @property
    def metric_bmi(self):
        return self.__metric_bmi

    # setter for self.__metric_bmi
    @metric_bmi.setter
    def metric_bmi(self, value):
        self.__metric_bmi = value

    # getter for self.__name
    @property
    def name(self):
        return self.__name

    # setter for self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    # function to write the results view
    def write_answer(self):
        page = self.__head + self.__main + self.__results_view + self.__error + self.__close
        page = page.format(**locals())
        return page

    # function to write the form view
    def write_form(self):
        page = self.__head + self.__main + self.__form + self.__error + self.__close
        page = page.format(**locals())
        return page
    
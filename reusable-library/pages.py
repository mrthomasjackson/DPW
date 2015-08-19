class Page(object):
    def __init__(self):
        self.__title = "BMI Utility"
        self.__css = "/css/styles.css"
        self.__message = "Please Fill Out The Following Form: "
        self.__returned_value = "answer"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
                    """
        self.__main = ""
        self.__form = """
        <div>
            <h1>{self.message}</h1>
        </div>
        <div>
            <form action="" method="GET">
            <label for='name'>Enter Your Name</label>
            <input type='text' name='name' id='name'></input></br>
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
            <label for="inches">:Inches</label></br>
            <label for='weight'>Weight (In Pounds)</label>
            <input type='text' name='weight' id='weight'/>


            <input class="" type="submit" name="submit" value="Submit" />
            </form>
        </div>
        """
        self.__results_view = '''
        <div>
            <span>Your BMI is </span><span>{self.returned_value}</span>
        </div>
        '''
        self.__body = ""
        self.__error = ""
        self.__close = """
    </body>
</html>
                    """

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, css):
        self.__css = css

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    @property
    def returned_value(self):
        return self.__returned_value

    @returned_value.setter
    def returned_value(self, value):
        pass

    def write_answer(self):
        page = self.__head + self.__main + self.__results_view + self.__error + self.__close
        page = page.format(**locals())
        return page

    def write_form(self):
        page = self.__head + self.__main + self.__form + self.__error + self.__close
        page = page.format(**locals())
        return page
class Page(object):
    def __init__(self):
        self.__title = "BMI Utility"
        self.__css = "/css/styles.css"
<<<<<<< HEAD
        self.__message = "Please Fill Out The Following Form: "
        self.__returned_value = "answer"
=======
        self.__message = "Please Select Conversion Type: "
>>>>>>> parent of 9de2ddc... Added Area and length views
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
                    """
<<<<<<< HEAD
        self.__main = ""
        self.__form = """
=======
        self.__main = """
>>>>>>> parent of 9de2ddc... Added Area and length views
        <div>
            <h1>{self.message}</h1>
        </div>
        <div>
            <form action="" method="GET">
<<<<<<< HEAD
            <label for='name'>Enter Your Name</label>
            <input type='text' name='name' id='name'></input></br>
            <select id='feet'>
                <option value='4'>4</option>
                <option value='5'>5</option>
                <option value='6'>6</option>
                <option value='7'>7</option>
                <option value='8'>8</option>
            </select>
            <label for="feet">:Feet</label>
            <select id='inches'>
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
            <input type='text id='weight'/>


            <input class="" type="submit" name="submit" value="Submit" />
            </form>
        </div>
        """


=======
            <label for="length">Length: </label>
            <select id="length" name="length">
                <option value="1" >First option</option>
                <option value="2" >Second option</option>
                <option value="3" >Third option</option>
            </select>
            <input class="button_text" type="submit" name="submit" value="Submit" />
            </form>
        </div>
        """
>>>>>>> parent of 9de2ddc... Added Area and length views
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
        self.print_out()

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body
        self.print_out()

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, css):
        self.__css = css
        self.print_out()

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message
        self.print_out()

    def print_out(self):
<<<<<<< HEAD
        all = self.__head + self.__main + self.__form + self.__error + self.__close
=======
        all = self.__head + self.__main + self.__body + self.__error + self.__close
>>>>>>> parent of 9de2ddc... Added Area and length views
        all = all.format(**locals())
        return all
class Page(object):
    def __init__(self):
        self.__title = "Conversion Utility"
        self.__css = "/css/styles.css"
        self.__message = "Please Select Conversion Type: "
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
        self.__select_conversion = """
        <div>
            <h1>{self.message}</h1>
        </div>
        <div>
            <form action="" method="GET">
            <label for="conversionType"></label>
            <select id="conversionType" name="conversionType">
                <option value="length" >Length</option>
                <option value="area" >Area</option>
            </select>
            <input class="" type="submit" name="submit" value="Submit" />
            </form>
        </div>
        """
        self.__length_view = '''
        <div>
            <form action='' method='GET'>
                <label for='select_length_unit_1'>Convert </label>
                <label for='length_input_1'></label>
                <input type='text' id='length_input_1'/>
                <select id='select_length_unit_1' name='select_length_unit_1'>
                    <option value="inches" >inches</option>
                    <option value="feet" >feet</option>
                    <option value="yards" >yards</option>
                    <option value="links" >links</option>
                    <option value="miles" >miles</option>
                </select>
                <span> to </span>
                <label for='select_length_unit_2'></label>
                <select id='select_length_unit_2' name='select_length_unit_2'>
                    <option value="inches" >inches</option>
                    <option value="feet" >feet</option>
                    <option value="yards" >yards</option>
                    <option value="miles" >miles</option>
                </select>
            <input class="" type="submit" name="submit" value="Submit" />
        </div>
        '''
        self.__area_view = '''
        <div>
            <form action='' method='GET'>
                <label for='select_length_unit_1'>Convert </label>
                <label for='length_input_1'></label>
                <input type='text' id='length_input_1'/>
                <select id='select_length_unit_1' name='select_length_unit_1'>
                    <option value="square_inches" >Square Inches</option>
                    <option value="square_feet" >Square Feet</option>
                    <option value="square_yards" >Square Yards</option>
                    <option value="square_miles" >Square Miles</option>
                </select>
                <span> to </span>
                <label for='select_length_unit_2'></label>
                <select id='select_length_unit_2' name='select_length_unit_2'>
                    <option value="square_inches" >Square Inches</option>
                    <option value="square_feet" >Square Feet</option>
                    <option value="square_yards" >Square Yards</option>
                    <option value="square_miles" >Square Miles</option>
                </select>
            <input class="" type="submit" name="submit" value="Submit" />
        </div>
        '''
        self.__answer_view = '''
        <div>
            <h2>{self.returned_value}</h2>
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

    @property
    def returned_value(self):
        return self.__returned_value

    @returned_value.setter
    def returned_value(self, returned_value):
        self.__returned_value = returned_value

    def print_length(self):
        the_view = self.__length_view + self.__answer_view
        the_view = the_view.format(**locals())
        return the_view

    def print_area(self):
        the_view = self.__area_view + self.__answer_view
        the_view = the_view.format(**locals())
        return the_view

    def print_out(self):
        all = self.__head + self.__main + self.__select_conversion + self.__error + self.__close
        all = all.format(**locals())
        return all
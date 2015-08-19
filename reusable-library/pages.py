class Page(object):
    def __init__(self):
        self.__title = "Conversion Utility"
        self.__css = "/css/styles.css"
        self.__message = "Please Select Conversion Type: "
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
                    """
        self.__main = """
        <div>
            <h1>{self.message}</h1>
        </div>
        <div>
            <form action="" method="GET">
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
        all = self.__head + self.__main + self.__body + self.__error + self.__close
        all = all.format(**locals())
        return all
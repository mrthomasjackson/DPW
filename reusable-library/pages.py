class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "/css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
                    """
        self.body = ""
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

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        all = all.format(**locals())
        return all
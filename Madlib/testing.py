__author__ = 'tjackson'

# print "Hello Mo!"
#
# string = "Hello Thomas"

# print string

# age = raw_input("How old are you?")
#
# rand = raw_input(" Give me a random number")
#
# random = int(age) * int(rand)

html = '''
<DOCTYPE! HTML>
    <html>
            <head>
                {title}
            </head>
            <body>
                {body}
            </body>
    </html>
'''

title = raw_input("Chose a title")

body = raw_input("Chose a body")

html.format(**locals())

print html






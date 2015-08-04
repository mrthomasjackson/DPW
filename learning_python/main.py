#I am trying python for the first time
__author__ = 'tjackson'

welcome_message = "Welcome!"
space = " "

#this is a one line comment
'''
Doc string (multiple line comments)
'''

first_name = "Thomas"
last_name = "Jackson"
#print(first_name + " " + last_name)

#response = raw_input("Enter Your Name")

#print welcome_message + space + response

birth_year = 1993
current_year = 2015
age = current_year - birth_year
#print age

print "You are " + str(age) + " years old"

budget = 10000

if budget > 100000:
    high_car = "A8"
    print "Yeah, I can afford an " + high_car
elif budget > 5000:
    print "Yay! You can afford a nice used car!"
else:
    # print "Don't get upset, but you may have to wait a while before buying a car."
    pass

characters = ["a","b","c"]
#print characters
characters.append("d")
#print characters
#print characters[2]

alphabet = dict() #initiate dictionary
alphabet = {"first": "a", "second": "b"}
print alphabet["first"]

#while loop
'''
i = 100
while i>0:
    print str(i) + " bottles on the wall"
    i -= 1

#for loop

for i in range(0, 100):
    print str(i), " bottles on the wall"
    i = i+1

#for each loop
family = ["Scott", "Jenny", "Thomas", "Ellen"]
for f in family:
    print f + " Jackson"


#functions

def convert_cm_in():
    request = int(raw_input("How many centimeters would you like to convert?"))
    inches = (request * 2.54)
    return inches

conversion = convert_cm_in()
print conversion
'''
#inputting variables into larger strings

title = "This is very useful."
body = "Yes, I agree with you."

html = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>
            {title}
        </title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
html = html.format(**locals())
print html



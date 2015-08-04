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

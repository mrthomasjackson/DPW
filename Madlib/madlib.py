__author__ = 'tjackson'

# Initiate Dictionary
dictionary = dict()

# Create Dictionary to hold nouns and verbs
dictionary = {"nouns": [], "verbs": []}

# Create array to hold number values
number_questions = []

# Add user input to the dictionary
dictionary["nouns"].append(raw_input("Name a place: "))
dictionary["nouns"].append(raw_input("Name a type of car: "))
dictionary["nouns"].append(raw_input("Who is your favorite super-villain? "))
dictionary["nouns"].append(raw_input("What is a popular children's toy? "))
dictionary["nouns"].append(raw_input("What type of toy did you just name? "))
dictionary["nouns"].append(raw_input("Name something really BIG: "))
dictionary["nouns"].append(raw_input("Let's hear a girls name: "))
dictionary["verbs"].append(raw_input("What is your favorite physical activity? "))
dictionary["verbs"].append(raw_input("Say something crazy! "))

# Add user input to the number array
number_questions.append(raw_input("How many countries have you traveled to? "))
number_questions.append(raw_input("What year were you born? "))
number_questions.append(raw_input("What is your favorite number? "))

# Function to create an equation with output
def numerical_playground(x,y):
    z = int(x) * int(y)
    return z

# Assign returned value from numerical_playground to "years_ago"
years_ago = numerical_playground(number_questions[0], number_questions[1])

# Create a second function to handle math formula
def numerical_classroom(x,y,z):
    a = int(x) * int(z)
    b = int(y) / a
    return b

# Assign returned value from numerical_classroom to "battles_won"
battles_won = numerical_classroom(number_questions[0], number_questions[1], number_questions[2])

# Family Guy Lib
family_guy = '''

*************************************************
*************************************************
*************************************************
>>>It seems today
>>>That all you see
>>>Is {dictionary[nouns][3]} in {dictionary[nouns][1]}
>>>And {dictionary[verbs][1]} on T.V
>>>
>>>But where are those good old-fashioned values....
>>>
>>>On which we used to rely?!
>>>
>>>Lucky there's a {dictionary[nouns][3]}!
>>>Lucky there's a man who
>>>Positively can do
>>>All the things that make us...
>>>
>>>{dictionary[verbs][0]} and cry!
>>>
>>>He's a {dictionary[nouns][3]}!
*************************************************
*************************************************
*************************************************

'''

# Star Wars Lib
star_wars = '''

*************************************************
*************************************************
*************************************************
>>>A long time ago ({number_questions[1]} years ago), in a {dictionary[nouns][0]} far,
>>>far away....
>>>
>>>It is a period of civil war.
>>>Rebel {dictionary[nouns][1]}, striking
>>>from a hidden base, have won
>>>their first victory against
>>>the evil {dictionary[nouns][2]}.
>>>
>>>During the battle, rebel
>>>spies managed to steal secret
>>>plans to the {dictionary[nouns][2]} ultimate weapon,
>>>the {dictionary[nouns][3]},
>>>an armored {dictionary[nouns][4]}
>>>with enough power to
>>>destroy an entire {dictionary[nouns][5]}.
>>>
>>>Pursued by the {dictionary[nouns][2]}'s
>>>sinister agents, Princess
>>>{dictionary[nouns][6]} {dictionary[verbs][0]} home aboard her
>>>starship, custodian of the
>>>stolen plans that can save
>>>her people and restore
>>>freedom to the {dictionary[nouns][1]}....
*************************************************
*************************************************
*************************************************
'''

# Asking if the user likes star wars or family guy
like_family_guy = raw_input("Do you like Family Guy? (yes or no): ")
if like_family_guy == "yes":
    family_guy = family_guy.format(**locals())
    print family_guy
else:
    pass


like_star_wars = raw_input("Do you like Star Wars? (yes or no): ")
if like_star_wars == "yes":
    star_wars = star_wars.format(**locals())
    print star_wars
else:
    pass

if like_family_guy and like_star_wars == "no":
    print "Your no fun... Why don't you re-run the script and choose Star Wars or Family Guy (or BOTH)..."





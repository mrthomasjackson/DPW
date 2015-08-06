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

# Function to create an equation with output "years_ago"
def numerical_playground(x,y):
    years_ago = x * y
    return years_ago



'''
A long time ago, in a galaxy far,
far away....

It is a period of civil war.
Rebel spaceships, striking
from a hidden base, have won
their first victory against
the evil Galactic Empire.

During the battle, rebel
spies managed to steal secret
plans to the Empire's
ultimate weapon, the DEATH
STAR, an armored space
station with enough power to
destroy an entire planet.

Pursued by the Empire's
sinister agents, Princess
Leia races home aboard her
starship, custodian of the
stolen plans that can save
her people and restore
freedom to the galaxy....
'''


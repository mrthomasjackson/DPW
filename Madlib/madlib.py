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
    z = x * y
    return z

# Assign returned value from numerical_playground to "years_ago"
years_ago = numerical_playground(number_questions[0], number_questions[1])

# Create a second function to handle math formula
def numerical_classroom(x,y,z):
    a = x * z
    b = y / a
    return b

# Assign returned value from numerical_classroom to "battles_won"
battles_won = numerical_classroom(number_questions[0], numerical_classroom[1], number_questions[2])

# Asking if the user likes star wars or family guy
like_star_wars = raw_input("Do you like Star Wars? (yes or no): ")
like_family_guy = raw_input("Do you like Family Guy? (yes or no): ")

# Play stories based on which user likes
if like_family_guy == "yes":
    family_guy = '''
It seems today
That all you see
Is {dictionary[nouns[2]]} in movies
And sex on T.V

But where are those good old-fashioned values....

On which we used to rely?!

Lucky there's a family guy!
Lucky there's a man who
Positively can do
All the things that make us...

Laugh and cry!

He's a Fam-ily Guyyy!
'''
    family_guy = family_guy.format(**locals())
    print family_guy
    
elif like_star_wars == "yes":
    star_wars = '''
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
elif like_family_guy and like_star_wars == "no":
    print "Your no fun... Why don't you re-run the script and choose Star Wars or Family Guy (or BOTH)..."





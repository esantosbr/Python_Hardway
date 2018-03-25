types_of_people = 10 # Put an integer number into variable 'types_of_people'

"""
Put a string containing variable 'types_of_people'
between some words into variable 'x'
"""
x = f"There are {types_of_people} types of people."

# Put strings into variable 'binary' and 'do_not'
binary = "binary"
do_not = "don't"

"""
Variable 'y' receives a string composed by new words plus
the content from variables 'binary' and 'do_not'
"""
y = f"Those who know {binary} and those who {do_not}."

# Print strings from variables 'x' and 'y'
print(x)
print(y)

# Print a new string composed by new words plus the content from variable 'x'
print(f"I said: {x}")

# Print a new string composed by new words plus the content from variable 'y'
print(f"I also said: '{y}'")

# Put the boolean value "False" into variable 'hilarious'.
# This must start wigh capital letter 'F'
hilarious = False

# Put an string in variable 'joke_evaluation' plus
# {} as a reference to insert another variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Print "joke_evaluation" string including content from variable 'hilarious'
print (joke_evaluation.format(hilarious))

# Put two differente strings into variables 'w' and 'e'
w = "This is the left side of..."
e = "a string with a right side."

# Print content from "w" and "e" togheter, as one big string.
print(w + e)

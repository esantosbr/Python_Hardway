# This is an easy way to use input() function.
# This way only value entered from the user will be into age variable
age = input("How old are you? ")
# If user insert 38 when asked for age and after use print(age)
# the printed value will be only 38 and not the string "How old are you? 38"
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

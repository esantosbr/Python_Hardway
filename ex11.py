# Make a question and don't end the line with a new line. end=''
print("How old are you? ", end='')
# Insert into variable 'age' a string received from user.
# input() is a function that receives a string from user.
# If you need another type of value you need to convert it before. 
age = input()
print("How tall are you? ", end='')
height = input()
print("How much do you weigh? ", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

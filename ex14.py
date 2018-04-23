from sys import argv

script, user_name, year = argv
answer = 'Your answer> '

print(f"Hi {user_name}, I'm the {script} script. We are in {year}")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(answer)

print(f"Where do you live {user_name}?")
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

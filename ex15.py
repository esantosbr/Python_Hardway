#import argv from sys module
from sys import argv
#Define variables to use argv
script, filename = argv
#Open file passed from user and return a stream to txt variable.
txt = open(filename)
#Print it's file name
print(f"Here's your file {filename}:")
#Print content readed from file defined in txt variable
print(txt.read())
#Asks the user to re-enter the file name
"""
print(f"Type the filename again:")
file_again = input(">")
#Open file name entered from user and return a stream to txt variable.
txt_again = open(file_again)
#Print content readed from file defined in txt_again variable
print(txt_again.read())
"""

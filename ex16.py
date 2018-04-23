from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
# Open the file provided when this application was started
# in write mode. If file don't exist it'll be created.
target = open(filename, 'w')
# Truncating a file to zero means discarding all its content:
# the file size becomes 0, so it becomes empty,
# but the file still exists on the filesystem.
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
# Asks the user for three strings
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# Writes the strings into file, breaking lines after each one.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Close the file.
print("And finally, we close it.")
target.close()

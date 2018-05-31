def callwhile(p1, p2, increment):

    numbers = []

    while p1 < p2:
        print(f"At the top i is {p1}")
        numbers.append(p1)

        p1 += increment
        print("Numbers now: ", numbers)
        print(f"At the botton i is {p1}")

print("Insert the starting number: ")
n1 = int(input("> "))

print("Insert the final number: ")
n2 = int(input("> "))

print("Insert incremental number: ")
inc_value = int(input("> "))

callwhile(n1, n2, inc_value)

print("The numbers: ")

for num in range(n1,n2):
    print(num)

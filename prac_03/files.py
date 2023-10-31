# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.

with open("name.txt", 'w') as out_file:
    name = input("Name: ")
    print(name, file=out_file)

# 2. Write code that opens "name.txt" and reads the name (as above) then prints, "your name is Bob" (or whatever name is in file).

with open("name.txt", 'r') as in_file:
    name = in_file.read()
    print(f"Your name is {name}")

# 3. Create a text file called number.txt and save it in your prac directory. Put the following three numbers on sperate lines in the file and save it like:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads onlt the first two numbers and adds them together then prints the result, which should be... 59.

in_file = open("numbers.txt", 'r')
number = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
print(number + number_two)


# Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

with open("numbers.txt") as in_file:
    total = 0
    for line in in_file:
        line_value = int(line.strip())
        total += line_value
        print(total)

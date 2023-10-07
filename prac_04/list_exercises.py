numbers = []
for i in range(5):
    number_of_numbers = int(input("Number: "))
    numbers.append(number_of_numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smaller number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / 5}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Username: ")
if name in usernames:
    print("Access Granted!!")
else:
    print("Access Denied!!")
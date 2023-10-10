numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0]
# # 3
numbers[-1]
# # 2
numbers[3]
# # 1
numbers[:-1]
# # [3, 1, 4, 1, 5, 9]
numbers[3:4]
# # 1
5 in numbers
# # True
7 in numbers
# # False
"3" in numbers
# # Flase
numbers + [6, 5, 3]
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Print all the elements from numbers except the first two (slice)
numbers[2:]
# Print whether 9 is an element of numbers
9 in numbers
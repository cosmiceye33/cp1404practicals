import random

NUMBER_PER_LINES = 6
MINIMUM = 1
MAXIMUM = 45


quick_picks = int(input("How many quick picks? "))
# for i in range(NUMBER_OF_LINES):
#     random_number = random.randrange(MINIMUM, MAXIMUM)
#     numbers.append(random_number)
    # number_in_line = [number for number in numbers if number in numbers]
# print(numbers)

for i in range(quick_picks):
    numbers = []
    for j in range(NUMBER_PER_LINES):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
    # numbers.clear()

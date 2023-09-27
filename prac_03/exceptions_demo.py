"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# when a str is entered instead of a number. For example, inputting "No" when asking for a price
2. When will a ZeroDivisionError occur?
# when a 0 is entered for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# have error checking so that the code can only continue if the denominator is not 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


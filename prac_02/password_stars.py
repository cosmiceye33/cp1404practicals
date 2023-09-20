"""
password length = 5
get input password
while length input password < password length:
    print to small of a password
    get input_password

for length input password:
    display * * length
"""

MINIMUM_PASSWORD_LENGTH = 5


def main():
    password = get_password()
    show_stars(password)


def show_stars(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("To small of a password")
        password = input("Password: ")
    return password


main()

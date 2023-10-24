"""
Emails
Estimated: 40 minutes
Actual: 43
"""


def main():
    """A program that prints an email from name."""
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        email = get_name_from_email(email, name_to_email)
    for name in name_to_email:
        print(f"{name.title()} ({name_to_email[name]})")


def get_name_from_email(email, name_to_email):
    """Gets a name from an email and checks if that is there name."""
    email = email.split("@")
    name = email[0].split(".")
    choice = input(f"Is your name {' '.join(name).title()}? (Y/n) ").lower()
    if choice == "" or choice == "y":
        name_to_email[" ".join(name)] = "@".join(email)
    else:
        user_name = input("Name: ")
        name_to_email[user_name] = "@".join(email)
    email = input("Email: ")
    return email


main()

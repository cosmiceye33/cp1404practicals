MENU = "(G)et a valid score \n (P)rint result \n (S)how stars \n (Q)uit"


def main():
    score = 0
    print(MENU)
    choice = input("").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            print(determine_score(score))
        elif choice == "s":
            print_stars(score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input("").lower()


def print_stars(score):
    print("*" * score)


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


main()

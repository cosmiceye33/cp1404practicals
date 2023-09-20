"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Name: ")
print(MENU)
choice = input("").upper()
while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("").upper()
print("Finished")

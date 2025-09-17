import os

def buildMenu(menuOptions):
    # Builds a menu from a list
    # Options are given a number used for selection
    # The first item of the list will be the menu name

    # Example:
    # List = ["Main Menu","Play","Options","Quit"]
    # ┌──┤Main Menu├──┐
    # │ 1. Play
    # │ 2. Options
    # │ 3. Quit
    # └ Choice: 
    
    print(f"┌──┤{menuOptions[0]}├──┐")

    for option in menuOptions[1:]:
        print(f"│ {menuOptions.index(option)}. {option}")

    choice = input("└ Choice: ")

    # if choice == "1":
    #     result = "You picked 1"
    # elif choice == "2":
    #     result = "You picked 2"
    # elif choice == "3":
    #     os.system("clear")
    # else:
    #     result = "Invalid Option!"

    return menuOptions[int(choice)]

menuOptions = []

while True:
    os.system("clear")
    
    try:
        print(f"    {selection}")
    except NameError:
        print( "    First Run")
        ...
    
    selection = buildMenu(["Main Menu","Play","Options","Quit"])


from display import open_message, show_options, costume_menu
from operations import rent_costume, return_costume


open_message()


continueLoop = True

while continueLoop:
    show_options()
    validInput = False
    while validInput == False:
        try:
            option = int(input("Enter an option: "))
            validInput = True
        except:
            print("******************************************")
            print("INVALID INPUT, Please enter a valid option")
            print("******************************************")
    if option == 1:
        costume_menu()
        rent_costume()
    elif option == 2:
        costume_menu()
        return_costume()
    elif option == 3:
        continueLoop = False
        print("Thank you for using our application")
    else:
        print("Please enter a valid option")

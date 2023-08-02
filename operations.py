from validate import validate_id, validate_quantity
from update import update_quantity
from invoice import generate_invoice, generate_return_invoice
from display import costume_menu


def rent_costume():
    cart = []
    rent_more = True
    while rent_more == True:
        costume_id = validate_id()
        costume_quantity = validate_quantity(costume_id)
        cart.append([costume_id-1, costume_quantity])
        update_quantity(costume_id-1, costume_quantity, "rent")
        response = input(
            "Do you want to rent more costumes? ( y for yes, any other key for no): ")
        if response.lower() != "y":
            rent_more = False
        else:
            costume_menu()
    generate_invoice(cart)


def return_costume():
    return_cart = []
    return_more = True
    while return_more:
        costume_id = validate_id()
        valid = False
        while valid == False:
            try:
                return_quantity = int(
                    input("Enter the quantity of Costume you want to Return: "))
                if return_quantity <= 0:
                    print("Cannot return <= 0 items. Enter again ")
                else:
                    valid = True
            except ValueError:
                print("Please enter numeric value on quantity!!")
        return_cart.append([costume_id-1, return_quantity])
        update_quantity(costume_id-1, return_quantity, "return")
        response = input(
            "Do you want to return more items?(y for yes, any key for no)")
        if response.lower() != "y":
            return_more = False
        else:
            costume_menu()
    generate_return_invoice(return_cart)

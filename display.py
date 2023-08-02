from read_file import file_data


def open_message():
    print("+-"*40)
    print("                         Costume Rental Application")
    print("+-"*40)


def show_options():
    print("""
Select an option
-- Press 1 to Rent a Costume
-- Press 2 to Return a Costume
-- Press 3 to Exit
    """)


def costume_menu():
    content = file_data()
    print("-"*65)
    print("ID\t", "Costume\t\t", "Brand\t\t", "Price\t", "Quantity", sep="")
    print("-"*65)
    id = 1
    for i in content:
        print(id, "    "+i.replace(",", "        "))
        id += 1

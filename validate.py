from read_file import file_data, get_costume_list


def validate_id():
    content = file_data()
    valid = False
    while valid == False:
        try:
            costume_id = int(
                input("Enter the id of Costume: "))
            if costume_id in range(1, len(content)+1):
                valid = True
            else:
                print("INVALID ID, Please enter a valid id from the available costumes")
        except ValueError:
            print("INVALID ID, Please enter a numeric vallue for id")
    return costume_id


def validate_quantity(id):
    costume_list = get_costume_list()
    valid = False
    print(int(costume_list[id-1][3]))
    if int(costume_list[id-1][3]) == 0:
        print("The costume is not available right now.")
        return 0
    print("The costume is available")
    while valid == False:
        try:

            quantity = int(input("Enter quantity of the costume: "))
            if quantity < 0 or quantity > int(costume_list[id-1][3]):
                print(
                    f"The quantity you entered is not available.Enter a value between 0 and {costume_list[id-1][3]} ")
            else:
                valid = True
        except ValueError:
            print("Please enter numberic value for quantity")
    return quantity

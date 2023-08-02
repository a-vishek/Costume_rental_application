from datetime import datetime
from read_file import get_costume_list


def generate_invoice(cart):
    costume_list = get_costume_list()
    name = input("Enter customer name: ")
    contact = input("Enter customer contact: ")
    total_price = 0
    rented_costumes = []
    rented_costumes_brand = []
    for i in cart:
        c_name = costume_list[i[0]][0]
        c_brand = costume_list[i[0]][1]
        c_price = int(costume_list[i[0]][2].strip("$"))
        rented_costumes.append(c_name)
        rented_costumes_brand.append(c_brand)
        total_price += c_price * i[1]

    date = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
    print("==================Costume Rental Invoice==============================")
    print(f"Costumer name: {name}")
    print(f"Costumer contact: {contact}")
    print(f"Date and Time of Rent: {date}")
    print(f"Rented costumes: {rented_costumes}")
    print(f"Rented costumes Brand: {rented_costumes_brand}")
    print(f"Total Price: {total_price}$")
    print(f"Thank you for using our service, {name}")
    print("NOTE: A fine of 1$ per day per costume if kept for more than 5 days")

    file = open(f"{date}_{name}.txt", "w")
    file.write(
        "--------------------------COSTUME RENTAL INVOICE----------------------------------\n")
    file.write(f"Name: {name} \n Contact Details: {contact}\n")
    file.write(f"Rented Items: {rented_costumes}\n")
    file.write(f"Rented Items Brand: {rented_costumes_brand}\n")
    file.write(f"Total price of all the costumes: {total_price}$\n")
    file.write(
        "---------------------------------------------------------------------------------")
    file.close()
    print("INVOICE IS GENERATED")


def generate_return_invoice(return_cart):
    costume_list = get_costume_list()
    name = input("Enter name: ")
    extra_days = int(
        input("If the Costume was kept for more than 5 days, Enter the no. of days: "))
    returned_costumes = []
    returned_costumes_brand = []
    fine = 1  # 1$ per day for each costume
    for i in return_cart:
        c_name = costume_list[i[0]][0]
        c_brand = costume_list[i[0]][1]
        #c_price = int(costume_list[i[0]][2].strip("$"))
        returned_costumes.append(c_name)
        returned_costumes_brand.append(c_brand)
    if extra_days > 0:
        fine = fine * len(return_cart) * extra_days
    else:
        fine = 0

    date = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
    print("==================Costume Rental Invoice RETURNED==============================")
    print(f"Costumer name: {name}")
    print(f"Date and Time of Rent: {date}")
    print(f"Rented costumes: {returned_costumes}")
    print(f"Rented costumes Brand: {returned_costumes_brand}")
    print(f"Fine: {fine}$")
    print(f"Thank you for using our service, {name}")

    file = open(f"{date}_{name}.txt", "w")
    file.write(
        "--------------------------COSTUME RENTAL INVOICE RETURNED----------------------------------\n")
    file.write(f"Name: {name}\n")
    file.write(f"Rented Items: {returned_costumes}\n")
    file.write(f"Rented Items Brand: {returned_costumes_brand}\n")
    file.write(f"Fine: {fine}$\n")
    file.write(
        "---------------------------------------------------------------------------------")
    file.close()
    print("INVOICE IS GENERATED")

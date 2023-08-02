from read_file import get_costume_list


def update_quantity(id, quantity, arg):
    costume_list = get_costume_list()
    file = open("costumes.txt", "w")
    if arg == "rent":
        costume_list[id][3] = int(costume_list[id][3]) - quantity
    elif arg == "return":
        costume_list[id][3] = int(costume_list[id][3]) + quantity
    for i in costume_list:
        file.write(i[0]+","+i[1]+","+i[2]+","+str(i[3])+"\n")
    file.close()
    print(get_costume_list())

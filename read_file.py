def file_data():
    file = open("costumes.txt", "r")
    content = file.readlines()
    file.close()
    return content


def get_costume_list():
    content = file_data()
    costume_list = []
    for i in range(len(content)):
        costume_list.append(content[i].strip("\n").split(","))
    return costume_list

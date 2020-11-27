def menu():
    print("1. Show all elements in dictionary")
    print("2. Add new item")
    print("3. Modify existing item")
    print("4. Delete existing item")
    print("x. End")


def show_all_elements():
    if len(dict.keys()) == 0:
        print("Dictionary is empty")
        return

    for key in dict.keys():
        print(dict[key], '\n', end="")


def add_new_item():
    new_key = input("Insert new key>>>")
    new_value = input("Insert new value>>>")

    if new_key in dict.keys():
        print("Key already exists!")
        return

    dict[new_key] = new_value


def modify_item():
    key = input("Insert key>>>")
    if key not in dict.keys():
        print("Key does not exist!")
        return

    new_value = input("Insert new value>>>")

    dict[key] = new_value


def delete_item():
    key = input("Insert key>>>")
    if key not in dict.keys():
        print("Key does not exist!")
        return
    dict.pop(key)


if __name__ == '__main__':
    global dict
    dict = {}

    while True:
        menu()
        option = input("Option>>>")

        if option == "1":
            show_all_elements()
        elif option == "2":
            add_new_item()
        elif option == "3":
            modify_item()
        elif option == "4":
            delete_item()
        elif option == "x":
            print("Shutting down")
            break
        else:
            print("Option does not exist")

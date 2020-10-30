schools = []


def print_meni():
    print("============Meni============")
    print("1. Show all schools.")
    print("2. Add new school.")
    print("3. Modify school.")
    print("4. Delete school.")
    print("x. End.")
    print("============================")


def show_all_schools():
    for school in schools:
        print(school, end=" ")
    print()


def add_new_school():
    school_name = input("Enter school name>>>")
    if school_name in schools:
        print("School already exits! You cannot add this school " + school_name)
    else:
        schools.append(school_name)
        print("School added successfully")


def modify_school():
    old_school_name = input("Which school would you like to modify>>>")
    if old_school_name in schools:
        new_school_name = input("New school name>>>")
        index_of_school = schools.index(old_school_name)

        schools[index_of_school] = new_school_name
        print("School modified successfully.")
    else:
        print("This school does not exist " + old_school_name)


def delete_school():
    school_to_delete = input("Which school would you like to delete>>>")

    if school_to_delete in schools:
        schools.remove(school_to_delete)
        print("School was successfully deleted!")
    else:
        print("This school does not exist " + school_to_delete)


if __name__ == '__main__':
    schools = ['School 1', 'School 2']
    while True:
        print_meni()

        option = input("Option>>>")

        if option == "1":
            show_all_schools()
        elif option == '2':
            add_new_school()
        elif option == '3':
            modify_school()
        elif option == '4':
            delete_school()
        elif option == "x":
            print("Kraj programa")
            break

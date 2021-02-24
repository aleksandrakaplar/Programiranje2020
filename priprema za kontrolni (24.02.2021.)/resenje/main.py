from kontrolni03.basket import Basket
from kontrolni03.fruit import Fruit

fruit_in_storage = []


def create_basket():
    global basket
    basket_id = input("Set basket id:")
    basket = Basket(basket_id)


def create_fruit():
    fruit_id = input("Set fruit id:")
    name = input("Set name of fruit:")
    type_of_fruit = input("Set type of fruit (apple, cherry, raspberry):")
    fruit = Fruit(fruit_id, name, type_of_fruit)
    fruit_in_storage.append(fruit)


def list_all_fruits_in_storage():
    for fruit in fruit_in_storage:
        print(fruit)


def get_fruit_list_of_fruits_by_index(fruit_id, fruits):
    index = -1
    for i in range(len(fruits)):
        if fruits[i].fruit_id == fruit_id:
            index = i
            break
    fruit = fruits[index]
    return fruit


def add_fruit_to_basket():
    fruit_id = input("Get fruit by fruit_id:")
    fruit = get_fruit_list_of_fruits_by_index(fruit_id, fruit_in_storage)
    fruit.add_to_basket(basket)
    basket + fruit


def remove_fruit_from_basket():
    fruit_id = input("Get fruit by fruit_id:")
    fruit = get_fruit_list_of_fruits_by_index(fruit_id, basket.fruits)
    fruit.remove_from_basket()
    basket - fruit


def list_all_fruits_in_basket():
    print(basket)


def list_fruits_by_type_in_basket():
    print(basket.list_fruits_by_type())


if __name__ == "__main__":
    while True:
        print("1. Create a basket")
        print("2. Create a fruit")
        print("3. List fruits in storage")
        print("4. Add fruit from storage to a basket")
        print("5. Remove fruit from basket")
        print("6. List all fruits in basket")
        print("7. List fruits from basket by type")
        print("x. End")

        option = input("Select option>>>")

        if option == "1":
            create_basket()
        elif option == "2":
            create_fruit()
        elif option == "3":
            list_all_fruits_in_storage()
        elif option == "4":
            add_fruit_to_basket()
        elif option == "5":
            remove_fruit_from_basket()
        elif option == "6":
            list_all_fruits_in_basket()
        elif option == "7":
            list_fruits_by_type_in_basket()
        elif option == "x":
            break
        else:
            print("Option not implemented!")

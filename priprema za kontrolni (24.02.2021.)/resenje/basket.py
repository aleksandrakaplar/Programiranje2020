from kontrolni03.fruit import Fruit


class Basket:

    def __init__(self, basket_id):
        self.basket_id = basket_id
        self.fruits = []
        self.numb_apples = 0
        self.numb_cherries = 0
        self.numb_raspberries = 0

    def __str__(self):
        result = ''
        for fruit in self.fruits:
            result += str(fruit)
        return result

    def __add__(self, fruit):
        if isinstance(fruit, Fruit):
            self.fruits.append(fruit)

            if fruit.type_of_fruit.lower() == "apple":
                self.numb_apples += 1
            elif fruit.type_of_fruit.lower() == "cherry":
                self.numb_cherries += 1
            elif fruit.type_of_fruit.lower() == "raspberry":
                self.numb_raspberries += 1

    def __sub__(self, fruit):
        if isinstance(fruit, Fruit):
            self.fruits.remove(fruit)
            if fruit.type_of_fruit.lower() == "apple":
                self.numb_apples -= 1
            elif fruit.type_of_fruit.lower() == "cherry":
                self.numb_cherries -= 1
            elif fruit.type_of_fruit.lower() == "raspberry":
                self.numb_raspberries -= 1

    def list_fruits_by_type(self):
        result_apple = ""
        result_cherry = ""
        result_raspberry = ""

        for fruit in self.fruits:
            if fruit.type_of_fruit == "apple":
                result_apple += str(fruit)
            elif fruit.type_of_fruit == "cherry":
                result_cherry += str(fruit)
            elif fruit.type_of_fruit == "raspberry":
                result_raspberry += str(fruit)

        final_result = ""

        if self.numb_apples > 0:
            final_result = f"Total number of apples {self.numb_apples}. \n List all apples\n" + result_apple

        if self.numb_cherries > 0:
            final_result += f"Total number of cherries {self.numb_cherries}. \n List all cherries\n" + result_cherry

        if self.numb_raspberries > 0:
            final_result += f"Total number of raspberries {self.numb_raspberries}. \n List all raspberries\n" + result_raspberry

        return final_result

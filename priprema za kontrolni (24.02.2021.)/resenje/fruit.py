class Fruit:

    def __init__(self, fruit_id, name, type_of_fruit):
        self.fruit_id = fruit_id
        self.name = name
        self.type_of_fruit = type_of_fruit
        self.basket = None

    def add_to_basket(self, basket):
        self.basket = basket

    def __str__(self):
        return f"Fruit: {self.name}, type of: {self.type_of_fruit}\n"

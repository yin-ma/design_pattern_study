from abc import ABC, abstractmethod


class Drink(ABC):
    def cost(self):
        pass

    def description(self):
        pass


class Coffee(Drink):
    def cost(self):
        return 50

    def description(self):
        return "basic coffee"


class AddOnDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink


class Milk(AddOnDecorator):
    def cost(self):
        return self.drink.cost() + 10

    def description(self):
        return self.drink.description() + " + milk"


class Caramel(AddOnDecorator):
    def cost(self):
        return self.drink.cost() + 20

    def description(self):
        return self.drink.description() + " + caramel"


if __name__ == "__main__":
    drink = Coffee()
    drink = Milk(drink)
    drink = Caramel(drink)

    print(drink.cost())
    print(drink.description())



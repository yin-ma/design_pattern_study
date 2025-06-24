from abc import ABC, abstractmethod


class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.pour()
        self.brew()
        self.add_condiments()

    def boil_water(self):
        print("boil water")

    def pour(self):
        print("pour")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    def brew(self):
        print("add tea")

    def add_condiments(self):
        print("add flower")


class Coffee(Beverage):
    def brew(self):
        print("add coffee powder")

    def add_condiments(self):
        print("add milk")


if __name__ == '__main__':
    tea = Tea()
    coffee = Coffee()

    tea.prepare()
    coffee.prepare()


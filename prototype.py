import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class GameCharactor(Prototype):
    def __init__(self, name, lvl, equipment):
        self.name = name
        self.lvl = lvl
        self.equipment = equipment

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"{self.name} | {self.lvl} | {self.equipment}")


if __name__ == "__main__":
    charactor1 = GameCharactor("john", 12, {"weapon": "sword", "armor": "light"})
    charactor1.display()

    charactor2 = charactor1.clone()
    charactor2.name = "peter"
    charactor2.lvl = 7
    charactor2.equipment = {"weapon": "staff", "armor": "heavy"}
    charactor2.display()
    charactor1.display()


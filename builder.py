from abc import ABC, abstractmethod

# product
class Meal:
    def __init__(self):
        self.menu = []

    def add(self, food):
        self.menu.append(food)

    def show(self):
        print("meal include : ", ", ".join(self.menu))


# builder
class MealBuilder(ABC):
    @abstractmethod
    def add_main_dish(self):
        pass

    @abstractmethod
    def add_side_dish(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class DailyMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_dish(self):
        self.meal.add("rice")

    def add_side_dish(self):
        self.meal.add("fish")

    def add_drink(self):
        self.meal.add("soup")

    def get_result(self):
        return self.meal


# director
class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_meal(self):
        self.builder.add_main_dish()
        self.builder.add_side_dish()
        self.builder.add_drink()
        return self.builder.get_result()


if __name__ == "__main__":
    builder = DailyMealBuilder()
    director = MealDirector(builder)

    meal = director.build_meal()
    meal.show()



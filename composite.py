from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("draw a circle")


class Square(Shape):
    def draw(self):
        print("draw a square")


class ShapeGroup(Shape):
    def __init__(self):
        self.children = []

    def add(self, shape):
        self.children.append(shape)

    def remove(self, shape):
        self.children.remove(shape)

    def draw(self):
        for s in self.children:
            s.draw()


if __name__ == "__main__":
    circle = Circle()
    square = Square()

    shape_group = ShapeGroup()
    shape_group.add(circle)
    shape_group.add(square)
    shape_group.draw()
    

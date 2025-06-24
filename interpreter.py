from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass


class Number(Expression):
    def __init__(self, val):
        self.val = val

    def interpret(self):
        return self.val


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()


if __name__ == '__main__':
    expr = Multiply(Add(Number(3), Number(2)), Number(5))
    result = expr.interpret()
    print(result)
    print((3 + 2) * 5)



class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

    def add(self, val):
        self.value += val


if __name__ == "__main__":
    obj1 = Singleton(10)
    obj2 = Singleton(20)
    print(obj1.value)
    print(obj2.value)

    obj1.add(3)
    print(obj1.value)
    print(obj2.value)

    obj2.add(5)
    print(obj1.value)
    print(obj2.value)

    print(obj1 == obj2)
    print(obj1)
    print(obj2)

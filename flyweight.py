class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def draw(self):
        print(f"draw tree {self.name}, {self.color}")


class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color):
        key = (name, color)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color)
        return cls._tree_types[key]


if __name__ == "__main__":
    forest = []

    acacia = TreeFactory.get_tree_type("acacia", "green")
    cherry = TreeFactory.get_tree_type("cherry", "pink")

    for _ in range(100):
        forest.append(acacia)
        forest.append(cherry)

    for tree in forest:
        tree.draw()






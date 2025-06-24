class Folder:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def accept(self, visitor):
        visitor.visit_folder(self)
        for item in self.items:
            item.accept(visitor)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def accept(self, visitor):
        visitor.visit_file(self)


class SizeCalculator:
    def __init__(self):
        self.total = 0

    def visit_file(self, file):
        self.total += file.size

    def visit_folder(self, folder):
        pass


if __name__ == '__main__':
    file1 = File("a.txt", 64)
    file2 = File("b.jpg", 256)

    sub_folder = Folder("img", [file2])
    root = Folder("root", [file1, sub_folder])

    calc = SizeCalculator()
    root.accept(calc)

    print(calc.total)



class MyIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


class MyCollection:
    def __init__(self):
        self._data = []

    def add(self, item):
        self._data.append(item)

    def __iter__(self):
        return MyIterator(self._data)


if __name__ == '__main__':
    collection = MyCollection()
    collection.add("apple")
    collection.add("banana")
    collection.add("orange")

    for fruit in collection:
        print(fruit)

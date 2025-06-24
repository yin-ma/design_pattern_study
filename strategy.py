from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSort(SortStrategy):
    def sort(self, data):
        print(f"using bubble sort {data}")


class QuickSort(SortStrategy):
    def sort(self, data):
        print(f"using quick sort {data}")


class Sorter:
    def __init__(self):
        self._strategy = QuickSort()

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        self._strategy.sort(data)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    sorter = Sorter()
    sorter.sort(data)
    sorter.set_strategy(BubbleSort())
    sorter.sort(data)


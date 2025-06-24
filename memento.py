class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class GameCharacter:
    def __init__(self):
        self.level = 1
        self.score = 0

    def play(self, level, score):
        self.level = level
        self.score = score
        print(f"level: {self.level}, score: {self.score}")

    def save(self):
        return Memento({"level": self.level, "score": self.score})

    def restore(self, memento):
        state = memento.get_state()
        self.level = state["level"]
        self.score = state["score"]
        print(f"restore level: {self.level}, score: {self.score}")


class History:
    def __init__(self):
        self._history = []

    def push(self, memento):
        self._history.append(memento)

    def pop(self):
        return self._history.pop() if self._history else None


if __name__ == '__main__':
    charactor = GameCharacter()
    history = History()

    charactor.play(10, 28)
    memonto = charactor.save()
    history.push(memonto)
    charactor.play(3, 11)
    charactor.restore(history.pop())





from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle(self):
        pass


class OffState(State):
    def handle(self):
        print(f"fan is off, switch to low speed")
        return LowSpeedState()


class LowSpeedState(State):
    def handle(self):
        print("fan is low speed, switch to high speed")
        return HighSpeedState()


class HighSpeedState(State):
    def handle(self):
        print("fan is high speed, switch to off")
        return OffState()


class Fan:
    def __init__(self):
        self._state = OffState()

    def set_state(self, state):
        self._state = state

    def press_button(self):
        self._state = self._state.handle()


if __name__ == '__main__':
    fan = Fan()
    fan.press_button()
    fan.press_button()
    fan.press_button()
    fan.press_button()


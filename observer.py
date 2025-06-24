class WeatherCenter:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def add(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, val):
        self._temperature = val
        self.notify()

    def notify(self):
        for obs in self._observers:
            obs.update(self._temperature)


class PhoneDisplay:
    def update(self, val):
        print(f"phone display temperature: {val}")


class ComputerDisplay:
    def update(self, val):
        print(f"computer display temperature: {val}")


if __name__ == '__main__':
    center = WeatherCenter()
    center.add(PhoneDisplay())
    center.add(ComputerDisplay())

    center.set_temperature(39)


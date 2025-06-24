from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


class TV(Device):
    def power_on(self):
        print("TV power on")

    def power_off(self):
        print("TV power off")


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.power_on()

    def turn_off(self):
        self.device.power_off()


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.turn_on()
    remote.turn_off()

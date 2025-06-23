from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass


class LightButton(Button):
    def render(self):
        print("light style button")


class DarkButton(Button):
    def render(self):
        print("dark style button")


class LightCheckBox(CheckBox):
    def render(self):
        print("light style checkbox")


class DarkCheckBox(CheckBox):
    def render(self):
        print("dark style checkbox")


class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class LightUIFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckBox()


class DarkUIFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckBox()


if __name__ == "__main__":
    light_ui = LightUIFactory()
    dark_ui = DarkUIFactory()

    light_ui.create_button().render()
    light_ui.create_checkbox().render()

    dark_ui.create_button().render()
    dark_ui.create_checkbox().render()


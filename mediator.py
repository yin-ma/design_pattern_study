from abc import ABC, abstractmethod


class ChatMediator(ABC):
    @abstractmethod
    def send(self, sender, message):
        pass


class ChatRoom(ChatMediator):
    def __init__(self):
        self.participants = []

    def register(self, user):
        self.participants.append(user)
        user.mediator = self

    def send(self, sender, message):
        for user in self.participants:
            if user != sender:
                user.receive(sender.name, message)


class User:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def send(self, message):
        print(f"{self.name} -> : {message}")
        self.mediator.send(self, message)

    def receive(self, sender_name, message):
        print(f"({self.name}) {sender_name} -> : {message}")


if __name__ == '__main__':
    room = ChatRoom()
    peter = User("peter")
    john = User("john")
    mary = User("Mary")

    room.register(peter)
    room.register(john)
    room.register(mary)

    peter.send("hello world!")




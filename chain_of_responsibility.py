from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass


class Level1Support(Handler):
    def handle(self, request):
        if request == "reset password":
            print("level1 handler: reset password")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("request rejected")


class Level2Support(Handler):
    def handle(self, request):
        if request == "server error":
            print("level2 handler: server error")
        elif self._next_handler:
            self._next_handler.handle(request)
        else:
            print("request rejected")


if __name__ == "__main__":
    support_chain = Level1Support()
    support_chain.set_next(Level2Support())

    support_chain.handle("reset password")
    support_chain.handle("server error")
    support_chain.handle("junk mail")

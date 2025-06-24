from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TextEditor:
    def __init__(self):
        self.content = ""

    def insert(self, text):
        self.content += text

    def remove(self, count):
        removed = self.content[-count:]
        self.content = self.content[:-count]
        return removed


class InsertCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.insert(self.text)

    def undo(self):
        self.editor.remove(len(self.text))


class DeleteCommand(Command):
    def __init__(self, editor, count):
        self.editor = editor
        self.count = count
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.editor.remove(self.count)

    def undo(self):
        self.editor.insert(self.deleted_text)


class CommandManager:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_stack.append(command)

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.history.append(command)


if __name__ == '__main__':
    editor = TextEditor()
    manager = CommandManager()

    manager.execute_command(InsertCommand(editor, "hello "))
    manager.execute_command(InsertCommand(editor, "world"))
    print(editor.content)

    manager.undo()
    print(editor.content)

    manager.redo()
    print(editor.content)

    manager.execute_command(DeleteCommand(editor, 6))
    print(editor.content)

    manager.undo()
    print(editor.content)



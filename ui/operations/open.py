from .operation import Operation

class Open(Operation):
    def description(self):
        return "Open Notepad"

    def run(self):
        self.console.open_notepad()
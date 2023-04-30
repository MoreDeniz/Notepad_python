from .operation import Operation

class Add(Operation):
    def description(self):
        return "Add note"

    def run(self):
        self.console.add_note()
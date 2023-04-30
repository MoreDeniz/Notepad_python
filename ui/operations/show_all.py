from .operation import Operation

class Show_all(Operation):
    def description(self):
        return "Show all notes"

    def run(self):
        self.console.show_all()

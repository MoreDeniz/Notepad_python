from .operation import Operation

class Exit(Operation):
    def description(self):
        return "Exit"

    def run(self):
        self.console.finish()
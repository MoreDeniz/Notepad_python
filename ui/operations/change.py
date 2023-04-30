from .operation import Operation

class Change(Operation):
    def description(self):
        return "Change note"

    def run(self):
        self.console.change_note()
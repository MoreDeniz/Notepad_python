from .operation import Operation

class Save(Operation):
    def description(self):
        return "Save"

    def run(self):
        self.console.save_note()
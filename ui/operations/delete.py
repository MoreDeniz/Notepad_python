from .operation import Operation
class Delete(Operation):
    def description(self):
        return "Delete note"

    def run(self):
        self.console.delete_note()

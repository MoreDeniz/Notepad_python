from .operation import Operation


class Selected_note(Operation):
    def description(self):
        return "Search by number"

    def run(self):
        self.console.selected_note()

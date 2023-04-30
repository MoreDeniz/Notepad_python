from .operation import Operation


class Search(Operation):
    def description(self):
        return "Select by date"

    def run(self):
        self.console.selected_notes()

from model.files_manager import Files_manager


class Controller:
    def __init__(self, view, notepad, path: str):
        self.view = view
        self.notepad = notepad
        self.view.set_controller(self)
        self.file = Files_manager(path)

    def open_file(self):
        self.notepad = self.file.load_notes(self.notepad)

    def save_file(self):
        self.file.save_notes(self.notepad)

    def not_empty(self):
        return self.notepad.not_empty()

    def get_size(self):
        return self.notepad.size()

    def show_all(self):
        return self.notepad.show_all()

    def add_note(self, new_title: str, new_content: str):
        self.notepad.add_note(new_title, new_content)

    def delete_note(self, idx: int):
        self.notepad.delete_note(idx)

    def change_note(self, idx: int, update_title: str, update_content: str):
        self.notepad.change_note(idx, update_title, update_content)

    def get_sorted_notepad(self, date: str):
        return self.notepad.sorted_notes(date)

    def get_search_note(self, idx: int):
        return self.notepad.search_note(idx)

    def notepad_table(self):
        return self.notepad.note_table

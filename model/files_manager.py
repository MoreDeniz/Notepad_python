import csv

from .note import Note
from .notepad import Notepad


class Files_manager:
    def __init__(self, path: str):
        self.path = path

    def load_notes(self, notepad: Notepad):
        try:
            with open(self.path, 'r', encoding='1251') as f:
                reader = csv.reader(f, delimiter=';')
                for idx, all_notes in enumerate(reader):
                    if idx:
                        notepad.get_notes().append(Note(all_notes[1],
                                                        all_notes[2],
                                                        all_notes[3],
                                                        all_notes[4]))
        except FileNotFoundError:
            raise Exception('File not found!')
        return notepad

    def save_notes(self, notepad: Notepad):
        with open(self.path, 'w', encoding='1251', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['№',
                             'Title',
                             'Content',
                             'Date of creation',
                             'Date of change'
                             ])
            for idx, note in enumerate(notepad.get_notes(), start=1):
                writer.writerow([idx,
                                 note.get_title(),
                                 note.get_content(),
                                 note.get_date_of_creation(),
                                 note.get_date_of_change()
                                 ])
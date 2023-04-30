
from datetime import datetime
from .note import Note
from tabulate import tabulate


class Notepad:
    def __init__(self):
        self.notes = []
        self.file_name = ''

    def get_notes(self):
        return self.notes

    def size(self):
        return len(self.notes)

    '''Добавить заметку'''
    def add_note(self, new_title: str, new_content: str):
        note = Note(new_title, new_content, datetime.today().strftime('%d.%m.%Y %H:%M'))
        self.notes.append(note)

    '''Показать список заметок'''
    def show_all(self):
        return self.notes

    def not_empty(self):
        return bool(self.notes)

    '''Удалить заметку'''
    def delete_note(self, idx: int):
        del self.notes[idx]

    '''Редактировать заметку'''
    def change_note(self, idx: int, new_title: str, new_content: str):
        self.notes[idx].change_note(new_title, new_content)

    @property
    def note_table(self):
        columns = ['№', 'Title', 'Content', 'Date of creation', 'Date of change']
        note_table = [[i,
                       note.get_title(),
                       note.get_content(),
                       note.get_date_of_creation(),
                       note.get_date_of_change()]
                      for i, note in enumerate(self.notes, start=1)]
        return tabulate(note_table, headers=columns, tablefmt='pipe')

    '''Сортировать заметки по дате'''

    def sorted_notes(self, date: str):
        columns = ['№', 'Title', 'Content', 'Date of creation', 'Date of change']
        note_table = [[i,
                       note.get_title(),
                       note.get_content(),
                       note.get_date_of_creation(),
                       note.get_date_of_change()]
                      for i, note in enumerate(self.notes, start=1)
                      if date in note.get_date_of_creation() or
                      date in note.get_date_of_change()]
        return tabulate(note_table, headers=columns, tablefmt='pipe')

    def search_note(self, idx: int):
        columns = ['№', 'Title', 'Content', 'Date of creation', 'Date of change']
        note_table = [[i,
                       note.get_title(),
                       note.get_content(),
                       note.get_date_of_creation(),
                       note.get_date_of_change()]
                      for i, note in enumerate(self.notes, start=1)
                      if i == idx + 1
                      ]
        return tabulate(note_table, headers=columns, tablefmt='pipe')

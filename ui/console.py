from .view import View
from .operations import Menu


class Console(View):
    on = False
    open = False
    save = True

    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    '''Начало работ, вывод Меню в консоль'''
    def start(self):
        if not self.open:
            self.controller.open_file()
            self.open = True
        self.on = True
        menu = Menu(self)
        while self.on:
            print(menu)
            idx = self.get_index(menu.menu_length(),
                                 "Select a menu item:\n")
            menu.run_menu(idx)

    '''Завершение работы, выход'''
    def finish(self):
        if self.save:
            self.on = False
            print("Exit")
            return
        if not self.open:
            self.controller.open_file()
            self.open = True
        yes_no = input("\nDo you want to save changes before closing(y/n)?")
        if yes_no == 'y':
            self.controller.save_file()
            self.save = True
            print("Changes saved")
        self.on = False
        print("\nShutdown...")

    @staticmethod
    def get_index(length: int, text: str):
        while True:
            user_input = input(text)
            if user_input.isdigit() and 0 <= int(user_input) < length:
                index = int(user_input)
                return index
            print(f"\n Input number: 0 - {length - 1}")

    '''Добавить новую заметку'''
    def add_note(self):
        new_title = input("\nInput title: \n")
        new_note = input("\nInput text: \n")
        self.controller.add_note(new_title, new_note)
        print("Note added\n")
        self.save = False

    '''Показать все заметки'''
    def show_all(self):
        if self.controller.not_empty():
            print("\n\t\tLIST OF NOTES:",
                  self.controller.notepad_table(), sep='\n')
        else:
            print("\n\t\tNO NOTES")

    '''Удалить заметку'''
    def delete_note(self):
        if not self.open:
            self.controller.open_file()
            self.open = True
        if self.controller.not_empty():
            idx = self.get_index(self.controller.get_size() + 1,
                                 "\nInput note number: ")
            if idx < 1 or idx > self.controller.get_size():
                print(f"Input number from 1 to {self.controller.get_size()}")
            else:
                self.controller.delete_note(idx - 1)
                self.save = False
                print("Note deleted")
        else:
            print("Notepad is empty")

    '''Выбрать заметку по номеру'''
    def selected_note(self):
        if not self.open:
            self.controller.open_file()
            self.open = True
        if self.controller.not_empty():
            idx = self.get_index(self.controller.get_size() + 1,
                                 "\nInput note number: ")
            if idx < 1 or idx > self.controller.get_size():
                print(f"Input number from 1 to {self.controller.get_size()}")
            else:
                print(f"\n\t\tNOTE FROM {idx}",
                      self.controller.get_search_note(idx - 1), sep='\n')
        else:
            print("Notepad is empty")

    '''Выбрать заметку по дате'''
    def selected_notes(self):
        if not self.open:
            self.controller.open_file()
            self.open = True
        if self.controller.not_empty():
            date = input("Input date: dd.mm.yyyy: ")
            print(f"\n\t\tNOTES FROM {date}",
                  self.controller.get_sorted_notepad(date), sep='\n')
        else:
            print("Notepad is empty")

    '''Редактировать заметку'''
    def change_note(self):
        if self.controller.not_empty():
            idx = self.get_index(self.controller.get_size() + 1,
                                 "\nInput note number: ")
            if idx < 1 or idx > self.controller.get_size():
                print(f"Input number from 1 to {self.controller.get_size()}")
            else:
                update_title = input("Update title or type 'ENTER':")
                update_note = input("Update note or type 'ENTER':")
                self.controller.change_note(idx - 1, update_title, update_note)
                self.save = False
                print("Note changed\n")
        else:
            print("Notepad is empty")

    def save_note(self):
        if not self.open:
            self.controller.open_file()
            self.open = True
        yes_no = input('Do you want to save changes?(y/n): ')
        if yes_no == 'y':
            self.controller.save_file()
            self.save = True
            print('Saved')
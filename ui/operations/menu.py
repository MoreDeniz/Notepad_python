from .add import Add
from .exit import Exit
from .save import Save
from .show_all import Show_all
from .change import Change
from .delete import Delete
from .search import Search
from .selected_note import Selected_note

class Menu:
    '''Методы Меню'''
    def __init__(self, console):
        self.options = []
        self.options.append(Exit(console))
        self.options.append(Add(console))
        self.options.append(Show_all(console))
        self.options.append(Selected_note(console))
        self.options.append(Search(console))
        self.options.append(Change(console))
        self.options.append(Delete(console))
        self.options.append(Save(console))

    '''Размер Меню'''
    def menu_length(self):
        return len(self.options)

    '''Запускает выбранный пункт Меню'''
    def run_menu(self, idx:int):
        option = self.options[idx]
        option.run()

    '''Вывод Меню'''
    def __str__(self):
        menu_str = "\n\t\tMENU:\n" \
                   "=====================\n"
        for idx, opt in enumerate(self.options, start=0):
            menu_str += f" {idx}. {opt.description()}\n"
        return menu_str





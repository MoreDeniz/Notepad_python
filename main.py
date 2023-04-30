from model.notepad import Notepad
from controller.notes_controller import Controller
from ui.console import Console


if __name__=='__main__':
    model = Notepad()
    ui = Console()
    controller = Controller(ui, model, 'notes.csv')
    ui.start()










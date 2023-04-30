from datetime import datetime

class Note:
    def __init__(self,
                 title: str,
                 content: str,
                 time_creation: str,
                 time_change: str = ''
                 ):
        self.n_title = title
        self.n_content = content
        self.date_of_creation = time_creation
        self.date_of_change = time_change

    '''Заголовок заметки'''
    def get_title(self):
        return self.n_title

    '''Основной текст заметки'''
    def get_content(self):
        return self.n_content

    '''Время создания заметки'''
    def get_date_of_creation(self):
        return self.date_of_creation

    '''Время редактирования заметки'''
    def get_date_of_change(self):
        return self.date_of_change

    '''Редактировать заметку'''
    def change_note(self, new_title: str, new_content: str):
        if new_title:
            self.n_title = new_title
        if new_content:
            self.n_content = new_content
        self.date_of_change = datetime.today().strftime('%d.%m.%Y %H:%M')
from view import *
from operations import *


def button_click():
    choice_main_menu = 0
    field_notes()
    while choice_main_menu != 5:
        choice_main_menu = show_main_menu()

        # Добавление новой заметки
        if choice_main_menu == 1:
            note = add_notes()
            record_data(note)

        # Чтение заметок
        if choice_main_menu == 2:
            choice_read_menu = 0
            while choice_read_menu != 3:
                choice_read_menu = show_read_menu()
                # Чтение всех имеющихся заметок
                if choice_read_menu == 1:
                    reading_all_notes()
                # Поиск заметок по дате создания
                if choice_read_menu == 2:
                    search_for_notes_by_date(input('Введите дату в формате ГГГГ-ММ-ДД: '))

        # Редактирование заметки
        if choice_main_menu == 3:
            choice_editing_menu = 0
            reading_all_notes()
            id = int(input("Введите ID заметки для редактирования: "))
            while choice_editing_menu != 3:
                choice_editing_menu = show_editing_menu()
                # Редактирование заголовка заметки
                if choice_editing_menu == 1:
                    editing_title_notes(id)
                # Редактирование тела заметки
                if choice_editing_menu == 2:
                    editing_body_notes(id)


        # Удаление заметки
        if choice_main_menu == 4:
            reading_all_notes()
            delete_notes(int(input("Введите ID заметки для удаления: ")))
            
        # Завершение работы программы
        if choice_main_menu == 5:
            print("До свидания!")

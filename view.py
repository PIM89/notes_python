# Проверка данных (ввод числа)

def verification(num):
    try:
        num = int(num)
        return True
    except:
        return False


# Вывод главного меню

def show_main_menu():
    print('\nДля добавления заметки введите - 1\n'
              'Для чтения заметок введите - 2\n'
              'Для редактирования заметок введите - 3\n'
              'Для удаления заметки введите - 4\n'
              'Для завершения работы программы введите - 5\n')
    choice = input("Поле для ввода: ")
    if verification(choice):
        return int(choice)
    else:
        show_main_menu()

# Вывод меню чтения заметок

def show_read_menu():
    print('\nДля вывода списка всех заметок введите - 1\n'
              'Для вывода списка заметок по дате создания (фильтр по дате) введите - 2\n'
              'Для возврата в главное меню введите - 3\n')
    choice = input("Поле для ввода: ")
    if verification(choice):
        return int(choice)
    else:
        show_read_menu()

# Вывод меню редактирования заметок

def show_editing_menu():
    print('\nДля редактирования заголовка заметки введите - 1\n'
              'Для редактирования тела заметки введите - 2\n'
              'Для возврата в главное меню введите - 3\n')
    choice = input("Поле для ввода: ")
    if verification(choice):
        return int(choice)
    else:
        show_editing_menu()
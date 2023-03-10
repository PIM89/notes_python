import os
import datetime

import pandas as pd

# Создание файла csv и заголовков таблицы

def field_notes():
    file_exists = os.path.isfile('notes.csv')
    if not file_exists:
        df = pd.DataFrame({'ID': [], 'Заголовок': [], 'Тело заметки': [
        ], 'Дата создания': [], 'Время создания': []})
        df.to_csv('notes.csv', sep=';', encoding='utf-8', index=False)

# Запись заметки в файл csv

def record_data(dictt):
    df = pd.DataFrame(dictt)
    df.to_csv('notes.csv', sep=';', encoding='utf-8',
              mode='a', header=None, index=False)
    print('\n')
    print(df)
    print('\nЗаметка сохранена!')


# Чтение всех имеющихся заметок

def reading_all_notes():
    print(pd.read_csv('notes.csv', sep=';'))

# Поиск заметок по дате и вывод результата

def search_for_notes_by_date(sttr):
    df = pd.read_csv('notes.csv', sep=';')
    indx = df.index[df['Дата создания'] == sttr]. tolist()
    print(df.loc[indx])

# Удаление заметки

def delete_notes(sttr):
    df = pd.read_csv('notes.csv', sep=';')
    indx = df.index[df['ID'] == sttr]. tolist()
    if not indx:
        print('Заметка с таким ID отсутствует!')
    else:
        df = df.drop(index=indx)
        df.to_csv('notes.csv', sep=';', encoding='utf-8', index=False)
        print('Заметка удалена!')

# Добавление новой заметки

def add_notes():
    heading = input('Введите заголовок заметки: ')
    content = input('Введите содержание заметки: ')
    date_time = str(datetime.datetime.now())
    df = pd.read_csv("notes.csv")
    notes_id = id(date_time)
    data = {'ID': [notes_id], 'Заголовок': [heading],
            'Тело заметки': [content], 'Дата создания': [date_time[0:10]], 'Время создания': [date_time[11:19]]}
    return data

# Редактирование заголовка заметки

def editing_title_notes(sttr):
    df = pd.read_csv('notes.csv', sep=';')
    indx = df.index[df['ID'] == sttr]. tolist()
    if not indx:
        print('Заметка с таким ID отсутствует!')
    else:
        heading = input('Введите новый заголовок заметки: ')
        df.loc[indx, 'Заголовок'] = heading
        df.to_csv('notes.csv', sep=';', encoding='utf-8', index=False)
        print('\nИзменения сохранены!')

# Редактирование тела заметки
     
def editing_body_notes(sttr):
    df = pd.read_csv('notes.csv', sep=';')
    indx = df.index[df['ID'] == sttr]. tolist()
    if not indx:
        print('Заметка с таким ID отсутствует!')
    else:
        content = input('Введите новый заголовок заметки: ')
        df.loc[indx, 'Тело заметки'] = content
        df.to_csv('notes.csv', sep=';', encoding='utf-8', index=False)
        print('\nИзменения сохранены!')
        
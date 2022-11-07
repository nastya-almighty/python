import sqlite3

def create_table():
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS school(
        student_id INTEGER,
        name TEXT,
        surname TEXT,
        bday TEXT,
        grade TEXT
    )   
    """)

    connect.commit()
    connect.close()

def check_existence(line):
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    cursor.execute('''SELECT surname FROM school WHERE surname=?''', (line,))
    exists = cursor.fetchall()
    if exists:
       return True
    else:
       return False

def create_query():
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    print('Добавляем новую запись в базу')
    st_list = []
    cursor.execute("SELECT Count(*) FROM school")
    count = cursor.fetchone()

    st_list.append((count[0] + 1))
    st_list.append(str(input('Введите имя ученика: ')).title())
    st_list.append(str(input('Введите фамилию ученика: ')).title())
    st_list.append(str(input('Введите дату рождения ученика: ')))
    st_list.append(str(input('В каком классе учится: ')))
    print(st_list)
    cursor.execute("INSERT INTO school VALUES(?, ?, ?, ?, ?);", st_list)
    print(f'Мы добавили следующую запись: {st_list}')
    connect.commit()
    connect.close()

def print_data(records):
    for row in records:
        print("ID:", row[0])
        print("Имя:", row[1])
        print("Фамилия:", row[2])
        print("Дата рождения:", row[3])
        print("Класс:", row[4], end="\n\n")


def select_query2(id):
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    select = """select * from school where student_id = ?"""
    cursor.execute(select, (id,))
    records = cursor.fetchall()
    print_data(records)
    connect.close()

def select_query1(sur):
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    if check_existence(sur):
        select = """select * from school where surname = ?"""
        cursor.execute(select, (sur,))
        records = cursor.fetchall()
        print_data(records)
    else:
        print('\nТакой записи не существует!\n')
    connect.close()

def delete_query():
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    sur = str(input('Введите фамилию для поиска: ')).title()
    if check_existence(sur):
        g = str(input('Если подтверждаете удаление, то введите любую цифру: '))
        if g.isdigit():
            cursor.execute("DELETE FROM school WHERE surname = ?", (sur,))
            print(f'Мы удалили из базы следующего человека: {sur}')
            connect.commit()
        else:
            print('Видимо, вы пока не готовы стереть этого человека из памяти!')
    else:
        print('Такой записи не существует!')
    connect.close()

def entire_book():
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM school;")
    all_results = cursor.fetchall()
    for i in all_results:
        print(i)
    connect.close()

def change_data():
    connect = sqlite3.connect('school.db')
    cursor = connect.cursor()
    key = str(input('Редактируем данные. Давайте найдем запись по фамилии: ')).title()
    select_query1(key)
    if check_existence(key):
        cursor.execute("SELECT student_id FROM school WHERE surname = ?", (key,))
        id = cursor.fetchone()
        print(id[0])
        c = int(input('Выберите номер строчки, данные которой хотите заменить: '))

        if c == 2:
            out = str(input('Введите новое имя: '))
            cursor.execute("UPDATE school SET name = ? WHERE student_id = ?", (out, id[0]))
        elif c == 3:
            out = str(input('Введите новую фамилию: '))
            cursor.execute("UPDATE school SET surname = ? WHERE student_id = ?", (out, id[0]))
        elif c == 4:
            out = str(input('Введите новую дату рождения: '))
            cursor.execute("UPDATE school SET bday = ? WHERE student_id = ?", (out, id[0]))
        elif c == 5:
            out = str(input('Введите новый номер класса: '))
            cursor.execute("UPDATE school SET grade = ? WHERE student_id = ?", (out, id[0]))
        else:
            print('Вы ввели неправильную команду, попробуйте еще раз!')
        connect.commit()
    connect.close()

        
import random
import re
import csv

def entire_book():
    with open('phonebook.csv', 'r', encoding = 'utf-8') as csv_file: 
        reader = csv.reader(csv_file) 
        for row in reader: 
            print(row)

def generate(N):
    with open('C:/Users/Acer/Desktop/geekbrains/python/home assignment/7/name_female.txt', 'r', encoding = 'utf-8') as fname:
        fname = fname.readlines()
    with open('C:/Users/Acer/Desktop/geekbrains/python/home assignment/7/name_male.txt', 'r', encoding = 'utf-8') as mname:
        mname = mname.readlines()
    with open('C:/Users/Acer/Desktop/geekbrains/python/home assignment/7/surname.txt', 'r', encoding = 'utf-8') as sur:
        sur = sur.readlines()
    with open('C:/Users/Acer/Desktop/geekbrains/python/home assignment/7/company.txt', 'r', encoding = 'utf-8') as com:
        com = com.readlines()

    with open('phonebook.csv', 'w', encoding = 'utf-8') as pb:
        f = lambda a: random.choice(a).replace('\n', ' ')
        for i in range(N):
            dir = ''
            dir += str(i + 1) + ' '
            x = random.randint(0, 1)
            if x:
                dir += f(fname)
                dir += random.choice(sur).replace('\n', 'а ')
            else:
                dir += f(mname)
                dir += f(sur)
            dir += str(random.randint(1940, 2000)) + ' '
            dir += f(com)
            dir += str(random.randint(79000000000, 79999999999))
            print(dir)
            pb.write(dir + '\n')
    return pb

def search(a):
    inp = open('phonebook.csv', 'r', encoding = 'utf-8').readlines()
    count = 0
    for i in iter(inp):
        if a in i.lower():
            print()
            print(i)
            count += 1
    if count == 0:
        print('Такой записи в справочнике нет')

def create_dir():
    inp = open('phonebook.csv', 'r', encoding = 'utf-8').readlines()
    new_dir = ''
    new_dir += str(len(inp) + 1) + ' '
    new_dir += str(input('Введите имя: ')) + ' '
    new_dir += str(input('Введите фамилию: ')) + ' '
    new_dir += str(input('Введите год рождения: ')) + ' '
    new_dir += str(input('Введите название компании: ')) + ' '
    
    y = int(input('Сколько телефонов вы хотите добавить? '))
    for i in range(y):
        new_dir += str(input('Введите номер телефона: ')) + ' '
    print(new_dir)
    new_dir += '\n'
    inp.append(new_dir)
    with open('phonebook.csv', 'w', encoding = 'utf-8') as pb:
        # csv_writer = csv.writer(pb)
        for item in inp:
            pb.write(str(item))

def change_data(a):
    inp = open('phonebook.csv', 'r', encoding = 'utf-8').readlines()
    newlines = []
    for i in range(len(inp)):
        count = 0
        if a in inp[i].lower():
            print()
            print(inp[i])
            i2 = str(inp[i].lower())
            w = str(input('Введите новые данные: '))
            x = re.sub(a, w, i2)
            inp[i] = (i2.replace(a, w)).title()
            newlines = inp
            print(x.title())
            count += 1
        with open ('phonebook.csv', 'w', encoding = 'utf-8') as pb:
            for i in iter(newlines):
                pb.write(i)
    if count == 0:
        print('Такой записи в справочнике нет')

def delete_data(a):
    inp = open('phonebook.csv', 'r', encoding = 'utf-8').readlines()
    count = 0
    newlines = []
    for i in iter(inp):
        if a in i.lower():
            print(i)
            count += 1
            g = str(input('Если подтверждаете удаление, то введите любую цифру: '))
            if g.isdigit():
                inp.remove(i)
                newlines = inp
                print(f'Мы удалили следующую запись: {i}')
            else:
                print('Видимо, вы пока не готовы стереть этого человека из памяти!')
        with open ('phonebook.csv', 'w', encoding = 'utf-8') as pb:
            for i in iter(newlines):
                pb.write(i)
    if count == 0:
        print('Такой записи в справочнике нет')
    

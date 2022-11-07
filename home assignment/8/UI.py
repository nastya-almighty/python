import tools as tl

print('Это база данных учеников школы')

def menu():
    while True:
        print('1. Показать весь список\n'
        '2. Поиск по фамилии\n'
        '3. Поиск по id записи\n'
        '4. Добавить новую запись\n'
        '5. Изменить запись\n'
        '6. Удалить запись\n'
        '7. Выйти из программы')
        n = int(input('Выберите пункт меню: '))

        if n not in range(1,8):
            print('Вы ввели неправильную команду, попробуйте еще раз!')

        if n == 1:
            tl.entire_book()

        elif n == 2:
            sur = str(input('Введите фамилию для поиска: ')).title()
            tl.select_query1(sur)

        elif n == 3:
            id = int(input('Введите номер id для поиска: '))
            tl.select_query2(id)
    
        elif n == 4:
            print('Создаем новую запись в справочнике.')
            tl.create_query()
    
        elif n == 5:
            tl.change_data()
    
        elif n == 6:
            print('Удаляем запись.')
            tl.delete_query()

        elif n == 7:
            print('До свидания!')
            exit()

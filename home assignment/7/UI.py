import tools as tl

print('Привет! Я телефонный справочник')

def menu():
    while True:
        print()
        print('1. Сгенерировать справочник')
        print('2. Поиск по фамилии')
        print('3. Поиск по номеру телефона')
        print('4. Добавить новую запись')
        print('5. Изменить запись')
        print('6. Удалить запись')
        print('7. Посмотреть справочник целиком')
        print('8. Выйти из программы')
        n = int(input('Выберите пункт меню: '))

        if n not in range(1,9):
            print('Вы ввели неправильную команду, попробуйте еще раз!')

        if n == 1:
            x = int(input('Сколько записей будет в вашем справочнике? '))
            tl.generate(x)

        elif n == 2:
            s = str(input('Введите фамилию для поиска в справочнике: ')).lower()
            tl.search(s)
    
        elif n == 3:
            num = str(input('Введите телефон для поиска в справочнике: '))
            if len(num) < 7:
                print('Маловато цифр, попробуйте еще!')
            else:
                tl.search(num)
    
        elif n == 4:
            print('Создаем новую запись в справочнике.')
            tl.create_dir()
    
        elif n == 5:
            key = str(input('Введите данные, которые хотите заменить: '))
            tl.change_data(key)
    
        elif n == 6:
            print('Удаляем запись.')
            key = str(input('Введите телефон или фамилию для поиска в справочнике: ')).lower()
            tl.delete_data(key)

        elif n == 7:
            tl.entire_book()

        elif n == 8:
            print('До свидания!')
            exit()
    


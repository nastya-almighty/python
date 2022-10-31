# Создайте программу для игры в ""Крестики-нолики"".

from PIL import Image, ImageFont, ImageDraw
import random

image = Image.new("RGB", (300, 300))
draw = ImageDraw.Draw(image)
draw.line((0, 100, 300, 100))
draw.line((0, 200, 300, 200))
draw.line((100, 300, 100, 0))
draw.line((200, 300, 200, 0))

fontsize = 20
font = ImageFont.truetype("arial.ttf", fontsize)

# не получилось сделать циклом, он отказывался брать переменную и рисовал какие-то белые квадраты вместо цифр
# for x in range(0, 300, 100):
#     for y in range (0, 300, 100):
#         for i in range(1, 10):
#             draw.text((x, y), f'{i}', font=font)

numbers = {
    1: (33, 33),
    2: (133, 33),
    3: (233, 33),
    4: (33, 133),
    5: (133, 133),
    6: (233, 133),
    7: (33, 233),
    8: (133, 233),
    9: (233, 233)
}

draw.text((5, 5), '1', font=font)
draw.text((105, 5), '2', font=font)
draw.text((205, 5), '3', font=font)
draw.text((5, 105), '4', font=font)
draw.text((105, 105), '5', font=font)
draw.text((205, 105), '6', font=font)
draw.text((5, 205), '7', font=font)
draw.text((105, 205), '8', font=font)
draw.text((205, 205), '9', font=font)

def Check(list):
    my_set = set(list)
    items = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for el in items:
        if (my_set.issuperset(el)):
            return True


print('Кто будет ходить первым?')
a = 1
turn = 0
choice = int(input('Нажмите 1, если хотите сделать первый ход, или любую другую цифру, если хотите отдать первый ход комьютеру. '))

if choice != 1:
    a = -a

image.show()
num = [i for i in range(1, 10)]
score_human = []
score_robot = []

fontsize = 60
font = ImageFont.truetype("arial.ttf", fontsize)
while turn < 9:
    if a == 1:
        x = int(input('В какой квадрат поставим крестик? '))
        if x not in num:
            print('Миша, давай по новой!')
            x = int(input('В какой квадрат поставим крестик? '))
        num.remove(x)
        score_human.append(x)
        draw.text((numbers[x]), 'x', font=font)
        image.show()

    else:
        print('Теперь сделает ход комьютер')
        x = random.choice(num)
        draw.text((numbers[x]), 'o', font=font)
        image.show()
        num.remove(x)
        score_robot.append(x)
    
    turn += 1
    a = -a
    if Check(score_robot):
        print()
        print('Пластмассовый мир победил!')
        exit()
    if Check(score_human):
        print()
        print('Вы победили!')
        print('Пока еще держим нашу оборону')
        exit()




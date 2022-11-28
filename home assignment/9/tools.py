from PIL import Image, ImageFont, ImageDraw
import random
from dict import numbers

def create_board():
    image = Image.new("RGB", (300, 300))
    draw = ImageDraw.Draw(image)
    draw.line((0, 100, 300, 100))
    draw.line((0, 200, 300, 200))
    draw.line((100, 300, 100, 0))
    draw.line((200, 300, 200, 0))

    fontsize = 20
    font = ImageFont.truetype("arial.ttf", fontsize)
    draw.text((5, 5), '1', font=font)
    draw.text((105, 5), '2', font=font)
    draw.text((205, 5), '3', font=font)
    draw.text((5, 105), '4', font=font)
    draw.text((105, 105), '5', font=font)
    draw.text((205, 105), '6', font=font)
    draw.text((5, 205), '7', font=font)
    draw.text((105, 205), '8', font=font)
    draw.text((205, 205), '9', font=font)
    image.show()
    return image

def Check_win(list):
    my_set = set(list)
    items = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for el in items:
        if (my_set.issuperset(el)):
            return True

def Game(choice):
    image = create_board()
    draw = ImageDraw.Draw(image)
    a = 1
    turn = 0
    if choice != 1:
        a = -a
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
        if Check_win(score_robot):
            print('\nПластмассовый мир победил!')
            exit()
        if Check_win(score_human):
            print('\nВы победили!\nПока еще держим нашу оборону')
            exit()

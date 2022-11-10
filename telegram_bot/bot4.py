import telebot
from telebot import types
from sympy import sympify
from datetime import datetime

API = '5680814143:AAFoF_x2A6iA3RNOQG-tMkxV9wo8S2xVZHg'
bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Калькулятор")
    btn2 = types.KeyboardButton("Справка")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f"Привет, {message.chat.first_name}! Я калькулятор".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Калькулятор"):
        msg = bot.send_message(message.chat.id, "Введите ваше выражение:")
        bot.register_next_step_handler(msg, handle_text)
        bot.register_next_step_handler(msg, log)
    elif(message.text == "Справка"):
        bot.send_message(message.chat.id, text="Используйте / для деления, * - для умножения, sqrt - для вычисления квадратного корня, ^ - чтобы возвести в степень.")


@bot.message_handler(content_types=["text"])
def handle_text(message):
        res = bot.send_message(message.chat.id, 'Ответ: ' + str(sympify(message.text)))


@bot.message_handler(content_types=['text'])
def log(message):
    a_log = open(f'log_{message.chat.id}.txt', 'a')
    a_log.write(f'{datetime.now()}, {message.chat.first_name}: {message.text} \n')


bot.polling(none_stop=True)
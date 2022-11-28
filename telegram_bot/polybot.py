import telebot
from sympy import sympify

API = '5988081324:AAGwY76gn0B91RY_SCD2QlrZ8el_WUsOFm8'
bot = telebot.TeleBot(API)


@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, text=f"Привет, {message.chat.first_name}! Я умею складывать многочлены. Пожалуйста, при введении многочленов не забудьте проставить знаки умножения");
    bot.send_message(message.chat.id, text=f"Введите первый многочлен");
    bot.register_next_step_handler(message, get_poly1)

def get_poly1(message):
    global poly1;
    poly1 = message.text.replace('=0' and '= 0', '')
    bot.reply_to(message, 'Введите второй многочлен');
    bot.register_next_step_handler(message, get_poly2);

def get_poly2(message):
    bot.register_next_step_handler(message, get_sum);
    global poly2;
    poly2 = message.text.replace('=0' and '= 0', '')
    get_sum(message)


def get_sum(message):
    newline = poly1 + "+" + poly2
    x = sympify(newline)
    bot.send_message(message.from_user.id, 'Сумма многочленов - ' + str(x))


bot.polling(none_stop=True)
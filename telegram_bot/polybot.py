import telebot
from sympy import sympify

API = '5988081324:AAGwY76gn0B91RY_SCD2QlrZ8el_WUsOFm8'
bot = telebot.TeleBot(API)

@bot.message_handler(content_types=['text'])
def star(message):
    bot.send_message(message.chat.id, text=f"Привет, {message.chat.first_name}! Я умею складывать многочлены.");
    bot.register_next_step_handler(message, get_poly1)
    bot.reply_to(message, 'Введите первый многочлен');

        

def get_poly1(message):
    global poly1;
    bot.register_next_step_handler(message, get_poly2);
    poly1 = message.text



def get_poly2(message):
    global poly2;
    bot.reply_to(message, 'Введите второй многочлен');
    bot.register_next_step_handler(message, get_sum);
    poly2 = message.text



def get_sum(message):
    newline = str(poly1)+ str(poly2)
    print(newline)
    print('ddddddd')    
   # x = sympify(newline)
    bot.send_message(message.from_user.id, 'Сумма многочленов ' + str(newline))

bot.polling(none_stop=True)
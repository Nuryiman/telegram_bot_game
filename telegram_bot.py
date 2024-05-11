import telebot
import random
from secret_tokens import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
list_for_knb = ['к', 'н', 'б']

@bot.message_handler(commands=['start', 'help', 'game'])
def starting(message):
    bot.send_message(message.chat.id, 'Здраствуйте, давайте поиграем в камень ножницы бумага')

@bot.message_handler(func=lambda message:True)
def knb(message):
    random_knb = random.choice(list_for_knb)
    if message.text.lower() == random_knb:
        bot.send_message(message.chat.id, 'НИЧЬЯ')
    elif message.text.lower() == 'к' and random_knb == 'н':
        bot.send_message(message.chat.id, 'Мой выбор ножницы и вы выиграли')
    elif message.text.lower() == 'к' and random_knb == 'б':
        bot.send_message(message.chat.id, 'мой выбор бумага и я выиграл')
    elif message.text.lower() == 'н' and random_knb == 'б':
        bot.send_message(message.chat.id, 'мой выбор бумага и вы выиграли')
    elif message.text.lower() == 'н' and random_knb == 'к':
        bot.send_message(message.chat.id, 'мой выбор камень и вы выиграли')
    elif message.text.lower() == 'б' and random_knb == 'к':
        bot.send_message(message.chat.id, 'мой выбор камень и вы выиграли')
    elif message.text.lower() == 'б' and random_knb == 'н':
        bot.send_message(message.chat.id, 'мой выбор ножницы и я выиграл')
    else:
        bot.send_message(message.chat.id, 'Вы ввели не верное значение, введите к или н или б')
bot.infinity_polling()

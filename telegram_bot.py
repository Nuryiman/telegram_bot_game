import telebot
import random
from secret_tokens import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


list_for_knb = ['к', 'н', 'б']


result = {}


@bot.message_handler(commands=['start', 'help', 'game'])
def starting(message):
    bot.send_message(message.chat.id, 'Здраствуйте, давайте поиграем в камень ножницы бумага, введите к или н или б')
    result[message.chat.id] = {'user': 0, 'bot': 0}


@bot.message_handler(func=lambda message:True)
def knb(message):

    random_knb = random.choice(list_for_knb)
    user_knb = message.text.lower()

    def users_counter():

        if message.chat.id in result.keys():
            result[message.chat.id] = {
                "user": result[message.chat.id]["user"] + 1,
                "bot": result[message.chat.id]["bot"]
            }
        else:

            result[message.chat.id] = {
                "user": 1,
                "bot": 0
            }

        bot.send_message(message.chat.id, str(result[message.chat.id]))

    def bots_counter():
        if message.chat.id in result.keys():
            result[message.chat.id] = {
                "user": result[message.chat.id]["user"],
                "bot": result[message.chat.id]["bot"] + 1
            }
        else:
            result[message.chat.id] = {
                "user": 0,
                "bot": 1
            }
        bot.send_message(message.chat.id, str(result[message.chat.id]))
    if user_knb == random_knb:
        bot.send_message(message.chat.id, 'НИЧЬЯ')
    elif user_knb == 'к' and random_knb == 'н':
        bot.send_message(message.chat.id, 'Мой выбор ножницы и вы выиграли')
        users_counter()
    elif user_knb == 'к' and random_knb == 'б':
        bot.send_message(message.chat.id, 'мой выбор бумага и я выиграл')
        bots_counter()

    elif user_knb == 'н' and random_knb == 'б':
        bot.send_message(message.chat.id, 'мой выбор бумага и вы выиграли')
        users_counter()

    elif user_knb == 'н' and random_knb == 'к':
        bot.send_message(message.chat.id, 'мой выбор камень и я выиграл')
        users_counter()

    elif user_knb == 'б' and random_knb == 'к':
        bot.send_message(message.chat.id, 'мой выбор камень и вы выиграли')
        users_counter()

    elif user_knb == 'б' and random_knb == 'н':
        bot.send_message(message.chat.id, 'мой выбор ножницы и я выиграл')
        bots_counter()
    else:
        bot.send_message(message.chat.id, 'Вы ввели не верное значение, введите к или н или б')


bot.infinity_polling()

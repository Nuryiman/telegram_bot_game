import telebot
from local_settings import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)
LOID = 7065054223

questions = ['Ваше любимое блюдо:', 'О чем вы мечтаете?', 'Какая ваша любимая марка машины?']
answer = []
ids = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать на опрос!')
    ids[message.chat.id] = {questions[0]: None}
    ids[message.chat.id] = {questions[1]: None}
    ids[message.chat.id] = {questions[2]: None}
    bot.send_message(message.chat.id, questions[0])

@bot.message_handler(func=lambda message: True)
def answers(message):
    ids[message.chat.id] = {questions[0]: message.text}
    bot.send_message(LOID, f'{message.from_user.first_name}: {message.text}')
    bot.send_message(message.chat.id, questions[1])
    if ids[message.chat.id][questions[0]: not None]:
        ids[message.chat.id] = {answer.append(message.text)}
    if ids[message.chat.id][questions[0]: not None] and ids[message.chat.id][questions[1]: not None]:
        ids[message.chat.id] = {questions[2]: message.text}


bot.infinity_polling()
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
    ids[message.chat.id] = {questions[0]: None, questions[1]: None, questions[2]: None}
    bot.send_message(message.chat.id, questions[0])
    print(ids)

@bot.message_handler(func=lambda message: True)
def answers(message):
    bot.send_message(LOID, f'{message.from_user.first_name}: {message.text}')
    if questions[0] in ids[message.chat.id].keys():
        bot.send_message(message.chat.id, questions[1])
    if questions[0] in ids[message.chat.id].keys():
        ids[message.chat.id] = {questions[1]: message.text}
        bot.send_message(message.chat.id, questions[2])
    if questions[1] in ids.keys():
        ids[message.chat.id][message.chat.id] = {questions[2]: message.text}
    else:
        ids[message.chat.id] = {questions[0]: message.text}
    print(ids)
    print(ids.keys())


bot.infinity_polling()
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
    ids[message.chat.id] = {}
    bot.send_message(message.chat.id, questions[0])
    print(ids)


@bot.message_handler(func=lambda message: True)
def answers(message):
    if questions[0] in ids[message.chat.id].keys() and questions[1] not in ids[message.chat.id].keys():
        ids[message.chat.id][questions[1]] = message.text
        bot.send_message(message.chat.id, questions[2])
        bot.send_message(LOID, f' {questions[1]}\n {message.from_user.first_name}: {message.text}')
    elif questions[1] in ids[message.chat.id].keys() and questions[2] not in ids[message.chat.id].keys():
        ids[message.chat.id][questions[2]] = message.text
        bot.send_message(message.chat.id, questions[2])
        bot.send_message(LOID, f' {questions[2]}\n {message.from_user.first_name}: {message.text}')
    else:
        ids[message.chat.id][questions[0]] = message.text
        bot.send_message(message.chat.id, questions[1])
        bot.send_message(LOID, f'{questions[0]}\n {message.from_user.first_name}: {message.text}')
    print(ids)
    print(ids.keys())


bot.infinity_polling()

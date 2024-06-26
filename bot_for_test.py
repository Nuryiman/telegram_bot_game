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
    if questions[1] in ids[message.chat.id].keys() and questions[2] not in ids[message.chat.id].keys():
        ids[message.chat.id][questions[2]] = message.text
        bot.send_message(message.chat.id, 'Спасибо за ответы), если хотите начать опрос заново напишите /start')
        bot.send_message(LOID, f' {questions[2]}\n {message.from_user.first_name}: {message.text}')
    elif questions[0] in ids[message.chat.id].keys() and questions[1] not in ids[message.chat.id].keys():
        ids[message.chat.id][questions[1]] = message.text
        bot.send_message(message.chat.id, questions[2])
        bot.send_message(LOID, f' {questions[1]}\n {message.from_user.first_name}: {message.text}')
    elif questions[0] not in ids[message.chat.id].keys():
        ids[message.chat.id][questions[0]] = message.text
        bot.send_message(message.chat.id, questions[1])
        bot.send_message(LOID, f'{questions[0]}\n {message.from_user.first_name}: {message.text}')
    else:
        bot.send_message(message.chat.id, 'Вы уже завершили опрос, если хотите начать заново нажмите /start')
    print(ids)


bot.infinity_polling()

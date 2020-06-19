import telebot, random
from telebot.types import Message
import vasya_conf as conf


token = conf.TOKEN
admin_id = conf.ADMIN_ID

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def vasya_answer(message: Message):
    if message.text.upper() == 'ДА':
        bot.reply_to(message, "Пизда! \U0001F604")
    if message.text.upper() == 'А':
        bot.reply_to(message, "Хуй на! \U0001F604")
    if message.from_user.id == admin_id and message.text.upper().find('ПОДТВЕРДИ') != -1:
        bot.reply_to(message, rnd_answer())


"""Бот отвечает на фото и видео смайликом"""
@bot.message_handler(content_types=['video', 'photo'])
def vasya_send_smile(message: Message):
    bot.send_message(message.chat.id, rnd_smiles())


"""Рандомные ответы"""
def rnd_answer():
    lst = ['Подтверждаю, это так! \U0001F60A',
           'Ну конечно же! \U0001F60C',
           'Ты совершенно прав!  \U0001F60E',
           'Да, это так! \U0001F609']
    return lst[random.randint(0, 3)]
def rnd_smiles():
    lst = ['\U0001F600',
           '\U0001F601',
           '\U0001F602',
           '\U0001F606',
           '\U0001F60E',
           '\U0001F604',
           '\U0001F605',
           '\U0001F638',
           '\U0001F640',
           '\U0001F63A',
           '\U0001F639']
    return lst[random.randint(0, 10)]

if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=60)
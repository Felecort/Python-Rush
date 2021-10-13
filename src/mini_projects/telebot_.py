import bot_key
import telebot
from telebot import types

bot = telebot.TeleBot(bot_key.token)


# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        # Подготовка кнопок
        bot.send_message(message.from_user.id, "Здарова, педики")
        keyboard = types.InlineKeyboardMarkup()
        key_place_1 = types.InlineKeyboardButton(text='1', callback_data='1')
        keyboard.add(key_place_1)
        key_place_2 = types.InlineKeyboardButton(text='2', callback_data='2')
        keyboard.add(key_place_2)

        # Отправка сообщения
        bot.send_message(message.from_user.id,
                         text='Выбери место',
                         reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Помоги себе сам!!!!")
    else:
        bot.send_message(message.from_user.id, "Каво?")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "1":
        msg = "Место 1: Корпус клоунов и дураков"
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "2":
        msg = "Место 2: Тут ебали Мать Вани Сотникова"
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)

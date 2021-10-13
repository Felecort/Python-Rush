"""
@eng_abobius_bot
"""

from bot_data import bot_key
from bot_data.bot_messages import *
from telebot import types
from telebot import TeleBot

bot = TeleBot(bot_key.token)


def attach_image():
    pass


def add_buttons():
        # Подготовка кнопок
        keyboard = types.InlineKeyboardMarkup()
        for i in range(5):
            button = types.InlineKeyboardButton(text=button_labels[i],
                                                callback_data=str(i))
            keyboard.add(button)
        return keyboard


# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.text).lower() in ("hello", "hi", "/help") :
        # Отправка сообщения
        keyboard_buttons = add_buttons()
        bot.send_message(message.from_user.id,
                         text=hello_message,
                         reply_markup=keyboard_buttons)
    else:
        bot.send_message(message.from_user.id,
                         text=unknown_message)


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    for i in range(5):
        if call.data == str(i):
            bot.send_message(call.message.chat.id,
                             button_mgs[i])


bot.polling(none_stop=True, interval=0)

"""
@eng_abobius_bot
"""

from bot_data import bot_key
from bot_data.bot_messages import *
from telebot import types
from telebot import TeleBot

bot = TeleBot(bot_key.token)
print("Bot started")


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
    if (message.text).lower() in ("hello", "hi", "/help", "/start") :        
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
            photo = open(photos_parth[i], 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                             button_mgs[i],
                             reply_markup=keyboard_buttons)


if __name__ == "__main__":
    keyboard_buttons = add_buttons()
    bot.polling(none_stop=True, interval=0)

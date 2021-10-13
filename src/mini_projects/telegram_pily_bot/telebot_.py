"""
@eng_abobius_bot
"""

# Импортирование констант
from bot_data.bot_key import *
from bot_data.bot_messages import *

# Импортирование API
from telebot import types
from telebot import TeleBot

# Запуск бота
bot = TeleBot(TOKEN)
print("Bot started")


# Создание кнопок
def add_buttons():
        keyboard = types.InlineKeyboardMarkup()
        for i in range(5):
            button = types.InlineKeyboardButton(text=BUTTON_LABELS[i],
                                                callback_data=str(i))
            keyboard.add(button)
        return keyboard


# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.text).lower() in ("hello", "hi", "/help", "/start") :        
        bot.send_message(message.from_user.id,
                         text=HELLO_MESSAGE,
                         reply_markup=keyboard_buttons)
    else:
        bot.send_message(message.from_user.id,
                         text=UNKNOWN_MESSAGE)


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    for i in range(5):
        if call.data == str(i):
            bot.send_photo(call.message.chat.id, PHOTO_LINKS[i])
            bot.send_message(call.message.chat.id,
                             BUTTON_MESSAGES[i],
                             reply_markup=keyboard_buttons)


# Точка входа
if __name__ == "__main__":
    keyboard_buttons = add_buttons()
    bot.polling(none_stop=True, interval=0)

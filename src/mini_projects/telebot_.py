"""
@eng_abobius_bot
"""

from bot_keys_ import bot_key
import telebot
from telebot import types
bot = telebot.TeleBot(bot_key.token)


def add_buttons():
        # Подготовка кнопок
        keyboard = types.InlineKeyboardMarkup()
        
        key_place_1 = types.InlineKeyboardButton(text='1', callback_data='1')
        keyboard.add(key_place_1)
        
        key_place_2 = types.InlineKeyboardButton(text='2', callback_data='2')
        keyboard.add(key_place_2)
        
        key_place_3 = types.InlineKeyboardButton(text='3', callback_data='3')
        keyboard.add(key_place_3)
        
        key_place_4 = types.InlineKeyboardButton(text='4', callback_data='4')
        keyboard.add(key_place_4)
        
        key_place_5 = types.InlineKeyboardButton(text='5', callback_data='5')
        keyboard.add(key_place_5)
        
        return keyboard


# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.text).lower() in ("привет", "/help") :
        # Отправка сообщения
        keyboard_buttons = add_buttons()
        bot.send_message(message.from_user.id,
                         text='Привет! Выбери место о котором хочешь узнать',
                         reply_markup=keyboard_buttons)
    else:
        bot.send_message(message.from_user.id, "Слишком сложно... Нприши привет или /help")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "1":
        msg = "Место 1: Корпус клоунов и дураков"
        bot.send_message(call.message.chat.id, msg)
        
    elif call.data == "2":
        msg = "Место 2: Тут ебали Мать Вани Сотникова"
        bot.send_message(call.message.chat.id, msg)
        
    elif call.data == "3":
        pass
    
    elif call.data == "4":
        pass
    
    elif call.data == "5":
        pass


bot.polling(none_stop=True, interval=0)

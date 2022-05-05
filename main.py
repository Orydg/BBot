"""
Телеграмм бот - БиБот

"""


import telebot
from telebot import types
import requests
from datetime import datetime
from auth_data import token


bot = telebot.TeleBot(token)


# телеграмм
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=1, )
    website = types.InlineKeyboardButton('Посетить Git', url='https://github.com/Orydg')
    markup.add(website)
    bot.send_message(message.chat.id, f'Привет, <b>{user_name}</b>!', parse_mode='html', reply_markup=markup)


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


# get_data()
bot.polling(none_stop=True)

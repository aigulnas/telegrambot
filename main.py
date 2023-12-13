import telebot
import random

from create_bot import bot

from handlers import welcome, send_help, send_answer, another_answer

def start_bot():
    bot.polling(none_stop=True)

if __name__=='__main__':
start_bot()

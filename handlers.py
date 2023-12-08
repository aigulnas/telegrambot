import telebot
import random

from create_bot import bot

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.reply_to(message, 'Привет! Я телеграм-бот. Чем могу помочь?')

@bot.message_handler(func=lambda message: message.text.lower() in ['привет', 'привет.', 'привет!', 'привет)'])
def send_help(message):
  bot.reply_to(message, 'Чем могу помочь?')

@bot.message_handler(func=lambda message: message.text.lower() in ['как дела?', 'как дела', 'как дела?)'])
def send_answer(message):
  answers = ['Хорошо!', 'Отлично!', 'Прекрасно!']
  bot.reply_to(message, random.choice(answers))

@bot.message_handler(func=lambda message: True)
def another_answer(message):
  bot.reply_to(message, 'Извините, я не понимаю ваше сообщение. Пожалуйста, попробуйте в другой раз.')
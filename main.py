import pymongo
from pymongo import MongoClient
import telebot
import datetime
bot = telebot.TeleBot('1427208327:AAH1iMuUqqPWU5BNja-bG9fl6nvA0fdBz0I')
@bot.message_handler(commands = ['start'])
def start(message):
    memberid = message.chat.id
    bot.send_message(memberid, 'Начало работы')
@bot.message_handler(commands = ['GetID'])
def main(message):
    memberid = message.chat.id
    bot.send_message(memberid, memberid)
    
bot.polling(none_stop=True)
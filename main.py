import json
import telebot
from telebot import apihelper

with open('config.json', 'r') as f:
    config = json.load(f)

TG_API_TOKEN = config['TG_API_TOKEN']
proxy = config['proxy']

apihelper.proxy = {'https':'socks5://{}:{}@{}:{}'.format(proxy['user'], proxy['password'], proxy['ip'], proxy['port'])}

bot = telebot.TeleBot(TG_API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Greetings! This bot will help you get some data from your image!\n\n<s>as if someone need it</s>", parse_mode='HTML')

bot.polling()
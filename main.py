import json
import telebot
from telebot import apihelper

from replies import replies

with open('config.json', 'r') as f:
    config = json.load(f)

TG_API_TOKEN = config['TG_API_TOKEN']
proxy = config['proxy']

apihelper.proxy = {'https':'socks5://{}:{}@{}:{}'.format(proxy['user'], proxy['password'], proxy['ip'], proxy['port'])}

bot = telebot.TeleBot(TG_API_TOKEN)

def sendTextMessage(message, text):
	bot.send_message(message.chat.id, text, parse_mode="HTML")

def handleWelcomeMessage(message):
	lang = 'en'
	if message.from_user.language_code == 'ru':
		lang = 'ru'

	sendTextMessage(message, replies['welcome'][lang])

def replyToPhoto(message):
	sendTextMessage(message, 'coming soon...')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	handleWelcomeMessage(message)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def echo_all(message):
	lang = 'en'
	if message.from_user.language_code == 'ru':
		lang = 'ru'
	content_type = message.content_type
	if content_type == 'photo':
		replyToPhoto(message)
		return
	sendTextMessage(message, replies['noPhoto'][lang])

bot.polling()
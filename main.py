import json
import telebot
# from telebot import apihelper
import os.path
import time
import PIL
from PIL import Image
import PIL.ExifTags

from texts import replies, additionalText
from utils import buildSuccessfulMessage, containesAnyNeededTag

with open('config.json', 'r') as f:
    config = json.load(f)

TG_API_TOKEN = config['TG_API_TOKEN']
# proxy = config['proxy']

# apihelper.proxy = {'https':'socks5://{}:{}@{}:{}'.format(proxy['user'], proxy['password'], proxy['ip'], proxy['port'])}

bot = telebot.TeleBot(TG_API_TOKEN)

def getLanguage(message):
	lang = 'en'
	if message.from_user.language_code == 'ru':
		lang = 'ru'
	# this weird way to define language is needed because value of message.from_user.language_code can be smth like 'en_GS' 'en_US' or even None.
	return lang

def getUsername(message):
	author = ''
	if bool(message.from_user.username):
		author = message.from_user.username
	else:
		author = 'id_{}'.format(message.from_user.id)
	return author

def sendTextMessage(message, text, is_reply=True):
	if is_reply:
		bot.reply_to(message, text, parse_mode="HTML", disable_web_page_preview=True)
	else:
		bot.send_message(message.chat.id, text, parse_mode="HTML", disable_web_page_preview=True)

def handleWelcomeMessage(message):
	sendTextMessage(message, replies['welcome'][getLanguage(message)], False)

def replyToPhoto(message):
	sendTextMessage(message, replies['photoIsNotSentLikeFile'][getLanguage(message)])

def checkDocument(message):
	execution_timer_start = time.time()
	file_info = bot.get_file(message.document.file_id)
	file_extension = os.path.splitext(file_info.file_path)[1]
	isExtensionValid = file_info.file_path.lower().endswith(('.heic', '.jpg', '.jpeg'))
	lang = getLanguage(message)
	if not isExtensionValid:
		sendTextMessage(message, replies['wrongFileExtention'][lang])
		return

	author = getUsername(message)

	download_start_time = time.time()
	file = bot.download_file(file_info.file_path)
	print('{} kb downloaded in: {} sec'.format(round(file_info.file_size / 1024, 2), round(time.time() - download_start_time, 5)))

	dirPath = "images/{}".format(author)
	newFileName = "image_{}{}".format(message.date, file_extension)

	isdir = os.path.isdir(dirPath)
	if not isdir:
		os.mkdir(dirPath)

	with open("{}/{}".format(dirPath, newFileName), 'wb') as new_file:
		new_file.write(file)
		THIS_FOLDER = os.path.dirname(os.path.abspath("{}/{}".format(dirPath, newFileName)))

	img = PIL.Image.open('{}\\{}'.format(THIS_FOLDER, newFileName))
	exif_data = img._getexif()

	if not bool(exif_data):
		sendTextMessage(message, replies['noExif'][lang])
		return

	exif = {
		PIL.ExifTags.TAGS[k]: v
		for k, v in img._getexif().items()
		if k in PIL.ExifTags.TAGS
	}

	if not containesAnyNeededTag(exif):
		sendTextMessage(message, replies['uselessExif'][lang])
		return

	file_data = {'ext': file_extension, 'size': round(file_info.file_size / 1024, 2)}

	execution_time = round(time.time() - execution_timer_start, 5)
	sendTextMessage(message, buildSuccessfulMessage(exif, file_data, execution_time, lang))


@bot.message_handler(commands=['start'])
def send_welcome(message):
	handleWelcomeMessage(message)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def echo_all(message):
	print(message.from_user)
	content_type = message.content_type
	if content_type == 'photo':
		replyToPhoto(message)
		return
	elif content_type == 'document':
		checkDocument(message)
		return
	sendTextMessage(message, replies['noPhoto'][getLanguage(message)])


bot.polling()

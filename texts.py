replies = {
	'welcome': {
		'ru': 'Здравствуйте! Этот бот может сообщить вам некоторые данные из ваших фотографий!\n\n<s>Круто же : (</s>',
		'en': '"Greetings! This bot will help you get some data from your image!\n\n<s>as if someone need it</s>'
	},
	'noPhoto':{
		'ru': 'Cорри, но нужно отправить именно <strong>фото</strong>!',
		'en': 'Apologies, but I can only process <strong>photos</strong>.'
	},
	'photoIsNotSentLikeFile':{
		'ru': 'К сожалению, при отправке фотки "быстрым" способом telegram удаляет из нее все данные.\nПоэтому нужно отправлять фото как <strong>ФАЙЛ</strong>',
		'en': 'Unfortunately, telegram deletes all data from image when it\'s sent in default way.\nPlease send image like <strong>FILE</strong>'
	},
	'wrongFileExtention':{
		'ru': 'Некорректный формат файла. Пожалуйста, используйте файлы с расширением <i>.jpg</>, <i>.jpeg</> или <i>.HEIC</>',
		'en': 'File extention is not valid. Please use file with <i>.jpg</>, <i>.jpeg</> or <i>.HEIC</> extentions'
	},
	'noExif':{
		'ru': 'К сожалению в этом изображении нет совсем никаких данных =( мб кто то стёр, хз...',
		'en': 'Unfortunately this file does\'nt contain any data at all'
	},
	'uselessExif':{
		'ru': 'В этом изображении нет никаких полезных данных',
		'en': 'This file does\'nt contain any useful data'
	},
	# 
	# 
	# 
	'success':{
		'ru': '''
Производитель устройства: {make},
Модель: {model},
Дата съёмки: {date}

GPS Координаты: {gps}

<strong><i>Технические особенности:</i></strong>
<i><strong>линзы:</strong> {lens}</i>
<i><strong>баланс белого:</strong> {white_bal}</i>
<i><strong>выдержка:</strong> {exposure_time} мс</i>

<strong><i>О файле:</i></strong>
<strong>расширение:</strong> {extension}
<strong>размер:</strong> {size} <i>кб.</i>

<i>обработано за {execution_time} сек</i>
		''',
		'en': '''
Device made by: {make},
Model: {model},
Date of shot: {date}

GPS coordinates: {gps}

<strong><i>Additional info:</i></strong>
<i><strong>lens:</strong> {lens}</i>
<i><strong>white balance:</strong> {white_bal}</i>
<i><strong>exposure time:</strong> {exposure_time} ms</i>

<strong><i>About file:</i></strong>
<strong>extension:</strong> {extension}
<strong>size:</strong> {size} <i>kb.</i>

<i>processed in  {execution_time} sec</i>
'''
	}
	#
	#
	#
}

additionalText = {
	'noData': {
		'ru': '<i>Нет данных</i>',
		'en': '<i>No info</i>'
	},
	'showMap': {
		'ru': 'Показать на карте',
		'en': 'Show on map'
	},
}

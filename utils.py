from datetime import datetime
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS

from texts import replies, additionalText

exifTitles = ('Make', 'Model', 'DateTimeOriginal', 'GPSInfo', 'LensModel', 'WhiteBalance', 'ExposureTime')

def containesAnyNeededTag(exif):
	result = False
	for tag in exifTitles:
		if tag in exif:
			result = True
	return result


def buildSuccessfulMessage(exif, file_data, execution_time, lang):
	formatted_exif = exif
	if 'DateTimeOriginal' in exif:
		date_time_str = str(exif['DateTimeOriginal'])
		date_time_obj = datetime.strptime(date_time_str, '%Y:%m:%d %H:%M:%S')
		result = str(date_time_obj.strftime("%d %B %Y %H:%M"))
		formatted_exif['DateTimeOriginal'] = result
	if 'ExposureTime' in exif:
		res = exif['ExposureTime'][0] / exif['ExposureTime'][1]
		formatted_exif['ExposureTime'] = round(res, 5)
	if 'GPSInfo' in exif:
			latLon = getLatLong(exif['GPSInfo'])
			if latLon != None:
				exif['GPSInfo'] = '{0}\n<a href="http://www.google.com/maps/place/{0}">{1}</a>'.format(latLon, additionalText['showMap'][lang])

	# if exif contains not ALL needed parameters, value of absent ones marked as absent
	finalTagList = {}
	value = additionalText['noData'][lang]
	for tag in exifTitles:
		finalTagList[tag] = value
		if tag in exif:
			finalTagList[tag] = exif[tag]
			pass

	return replies['success'][lang].format(
		make = finalTagList['Make'],
		model = finalTagList['Model'],
		date = finalTagList['DateTimeOriginal'],
		gps = finalTagList['GPSInfo'],
		white_bal = finalTagList['WhiteBalance'],
		lens = finalTagList['LensModel'],
		exposure_time = finalTagList['ExposureTime'],
		extension = file_data['ext'],
		size = file_data['size'],
		execution_time = execution_time,
	)


def getLatLong(GPSInfo):

	keys = GPSInfo.keys()
	result = {}
	for key in keys:
		if key in GPSInfo and key in GPSTAGS:
			result[GPSTAGS[key]] = GPSInfo[key]

	if len(result.keys()) > 1:
		return get_coordinates(result)
	else:
		return None

def get_decimal_from_dms(dms, ref):
	degrees = dms[0][0] / dms[0][1]
	minutes = dms[1][0] / dms[1][1] / 60.0
	seconds = dms[2][0] / dms[2][1] / 3600.0
	if ref in ['S', 'W']:
		degrees = -degrees
		minutes = -minutes
		seconds = -seconds

	return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
	lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
	lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

	return '{}, {}'.format(lat, lon)
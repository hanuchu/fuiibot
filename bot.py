from twython import Twython, TwythonError
from PIL import Image
import os, random, statistics, time

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

brightness_threshold = 35
seconds_between_tweets = 600

def tweet():
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	acceptable = False
	while not acceptable:
		fn = '.'
		while fn.startswith('.'):
			fn = random.choice(os.listdir('img/'))
			acceptable = image_acceptable('img/' + fn)

	photo = open('img/' + fn, 'rb')
	response = twitter.upload_media(media=photo)

	try:
		twitter.update_status(status='#FutureDiaryBot #MiraiNikki #FutureDiary' + ' ', media_ids=[response['media_id']])
		print 'tweeted!'
	except TwythonError as error:
		print error

def main():
	while True:
		tweet()
		time.sleep(seconds_between_tweets)

def image_acceptable(path):

	img = Image.open(path)
	all_rgb = []

	pix = img.load()
	for x in range(0, img.size[0]):
		for y in range(0, img.size[1]):
			all_rgb.append(pix[x,y])

	all_brightness = map(sum, all_rgb)
	sd = statistics.stdev(all_brightness)

	return sd > brightness_threshold

main()

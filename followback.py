from twython import Twython, TwythonStreamer, TwythonError

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
    	if 'event' in data and 'target' in data and 'source' in data:
    		if data['event'] == 'follow' and data['target']['screen_name'] == 'FutureDiaryBot':
    			twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    			try:
    				twitter.create_friendship(user_id = data['source']['id'])
    				print 'auto followed @' + data['source']['screen_name']
    			except TwythonError as error:
    				print error

    def on_error(self, status_code, data):
        print status_code, data

def main():
	stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	stream.user()

main()

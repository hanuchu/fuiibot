from twython import Twython
import webbrowser

APP_KEY = ''
APP_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

webbrowser.open(auth['auth_url'])

pin = raw_input('pin\n')

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(pin)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

print OAUTH_TOKEN
print OAUTH_TOKEN_SECRET

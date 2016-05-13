So, you want to use this bot yourself eh?  

First, you want to download the zip file because where would you post your stuff  
Head over to Twitter Application Management to create a new app  
After creating the app, copy your app's Consumer Key (API Key) and Consumer Secret (API Secret) and paste them into the file auth.py as the value of variables APP_KEY and APP_SECRET  
Run auth.py and follow the instruction  
Get the value of your OAUTH_TOKEN and OAUTH_TOKEN_SECRET printed in terminal  
Open up bot.py and follow-back.py and paste in the values of APP_KEY, APP_SECRET, OAUTH_TOKEN and OAUTH_TOKEN_SECRET  
A test video clip and some test images have been included in the video and img folder. If you want to use your own video(s) to get the images to tweet, simply delete all contents in the two folders and put your video file(s) into the video folder. Run video2frames.py and frames will be extracted and saved into the img folder  
Run bot.py and a random image in the img folder will be tweeted every 10 min  
If you want the bot to instantly follow back its new followers, run follow-back.py as well  

import telepot
import time
import os
import random
f = open("api_key", "r")
token= f.read()
print token
TelegramBot = telepot.Bot(token[:-1])
updates=TelegramBot.getUpdates()
n_length=len(updates)
while True:
    if len(updates) > n_length:
        chat_id= updates[-1]['message']['chat']['id']
        print(updates[-1]['message']['from']['username']+ ' ' + updates[-1]['message']['text'])
        if updates[-1]['message']['text'].find('HollySenzaBenji'):
		path = '~/Holly'
                files = os.listdir(path)
                i= random.randint(0, len(files)-1)
                photo= files[i]
                sendPhoto(chat_id, photo)
        updates=TelegramBot.getUpdates()
        n_length= len(updates)
    time.sleep(0.1)
    updates=TelegramBot.getUpdates()
    

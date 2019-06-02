import telepot
import time
token= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TelegramBot = telepot.Bot(token)
updates=TelegramBot.getUpdates()
n_length=len(updates)
while True:
    if len(updates) > n_length:
        chat_id= updates[-1]['message']['chat']['id']
        print(updates[-1]['message']['from']['username']+ ' ' + updates[-1]['message']['text'])
        n_length=len(updates)
        user_input = raw_input('Michael: ')

        TelegramBot.sendMessage(chat_id, user_input)
    time.sleep(0.1)
    updates=TelegramBot.getUpdates()
    

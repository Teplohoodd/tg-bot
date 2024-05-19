from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import random
import time
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Getting api data
api_id = config['login']['api_id']
api_hash = config['login']['api_hash']
phone = "your phone"
timer = 1000

#username1 = "" 
username2 = "" 
#username3 = "" 
#username4 = "" 
#username5 = "" 
#username6 = "" 

client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
chats = []
last_date = None
chunk_size = 10
groups=[]
result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
chats.extend(result.chats)
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
while True:
    try:
        msgtosend = random.choice(list(config['message']))#MESSAGE TO SEND
        #msg = client.send_message(username1, msgtosend)
        msg1 = client.send_message(username2, msgtosend)
        #msg2 = client.send_message(username3, msgtosend)
        #msg3 = client.send_message(username4, msgtosend)
        #msg4 = client.send_message(username5, msgtosend)
        #msg5 = client.send_message(username6, msgtosend)
        print("Send Complete!!, Waiting for " + str(timer) + " seconds")
        time.sleep(timer)
    except:
        continue

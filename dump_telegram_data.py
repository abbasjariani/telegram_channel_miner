#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 00:04:48 2019

@author: abbas
"""

# api_id and api_hash from https://my.telegram.org, under API Development.
# replace XXX and 'XXX' with what you see on the above link

api_id= XXX
api_hash = 'XXX'

from telethon import TelegramClient, events, sync
from telethon import utils
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
   

client = TelegramClient('session_name', api_id, api_hash)
client.start()




me = client.get_me()
print(me.stringify())

chats = client.get_dialogs()



for chat in chats:
    #dir(chat)
    if chat.name == "*میثم صمدی*":
        mes_chat = chat
        print("Found Meysam Samadi's group")
        dir(mes_chat)
        #chat.is_channel
        mes_chat.dialog.stringify()
                
        sam_g_entity = mes_chat.entity
        sam_g_entity.to_dict()
        sam_g_msg = mes_chat.message
        sam_g_msg.to_dict()
        
        chat_id = sam_g_entity.id

        
help(client.get_messages)

msg_hist =  client.get_messages(mes_chat, limit=1000000)


#Dump msg_hist into json format

        

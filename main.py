"""
Title:  slack_bot_main
Desc:   The main script which runs the slack bot
Author: Yassin Eltahir
Date:   2017-02-18
"""


import time
import yaml
from slackclient import SlackClient
from command_handler import *


# Source Config
conf = yaml.load(open('conf.eyaml','r'))

# Global Variables
bot_id = conf['slack']['botID']  # Bot User Name/ID
bot_name = "<@" + bot_id + ">"
default_channel = 'bot_test'
refresh_rate = 1       # Define refresh rate (sec) for bot to look for new messages


# Create slack client
api_token = conf['slack']['apiToken']
sc = SlackClient(api_token)


# Connect & Launch Bot
try:
    sc.rtm_connect()
    sc.rtm_send_message(default_channel,"ADS Bot is locked, loaded and ready to roll")
    
    while True:
        msg, usr, chnl = parseMessage(sc.rtm_read())
        if msg and usr and chnl:          
            parseCommand(msg, usr, chnl, sc)
        # Wait & check for new messages
        time.sleep(refresh_rate)

except:
    print("Bot failed... :(")


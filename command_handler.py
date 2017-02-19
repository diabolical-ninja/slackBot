"""
Title:  command_handler
Desc:   Contains parsing functions to handle commands thrown at slack bot
Author: Yassin Eltahir
Date:   2017-02-18
"""

from jokes import jokes
import re
import yaml
from metric_calcs import metricFunctions

# Source Config
conf = yaml.load(open('conf.eyaml','r'))

# Global Variables
bot_id = conf['slack']['botID']  # Bot User Name/ID
bot_name = "<@" + bot_id + ">"



# Clean up message
def cleanString(message):
    out = message.lower()  # Lower Case
    out = re.sub('[^A-Za-z0-9]+',' ',out) # Remove special characters
    return out


# Find preceeding word
def prevWord(target, source):
    source = source.split()
    for i,w in enumerate(source):
        if target in w:
            return source[i-1]
    


def parseMessage(rtm_output):
    """
    Takes the output from rtm_read() & determines if the bot should be engaged
    """
    
    # Check if anything is present
    if len(rtm_output) > 0:
        for slack_message in rtm_output:
            if slack_message and 'text' in slack_message and bot_name in slack_message["text"]:

                # Return message, user & channel
                msg = slack_message["text"].split(bot_name)[1].strip()
                usr = slack_message["user"]
                chnl = slack_message["channel"]

                return msg, usr, chnl
            
    return None, None, None



def interpretQuestion(question):
    '''
    Takes the users question as input & determines:
        - Which vertical, time range & metric it pertains to
    '''
    # Clean up question string
    question = cleanString(question)
    
    # Terms for Vertical, time range & metric to calculate
    verticals = ['health','energy','life','broadband','gi','movers','home']
    metrics = ['conversion','contact rate', 'connect rate','rps']
    time_names = ['minute','hour','day','week','month','year']
    
    
    # Identify question parameters
    wanted_verticals = [x for x in verticals if question.count(x) > 0]
    wanted_metrics = [x for x in metrics if question.count(x) > 0]
    wanted_datetime = [[x,prevWord(x,question)] for x in time_names if question.count(x) > 0]
    
    if len(wanted_metrics) > 0 and len(wanted_verticals) > 0 and len(wanted_datetime) > 0:
        return wanted_verticals, wanted_metrics, wanted_datetime
    else:
        return None, None, None
    
    



def parseCommand(message, user, channel, con):
    """
    Takes the message, determines what is being asked for & runs the corresponding command
    If it's unable to figure out the command it will ask for clarification
    """

    if 'how' in message and 'are' in message and 'you' in message:
        user_name = "<@" + user + ">"
        response = "Hey {}, I'm great! How can I help you?".format(user_name)

    elif 'joke' in message:
        response = jokes()
    else:
        # Extract question details from string
        vertical, metric, dateTime = interpretQuestion(message)

        if None in (vertical, metric, dateTime):
            response = "Sorry, I wasn't able to understand your question"
        else:
            response = metricFunctions.funcDict[metric[0]](vertical, dateTime)
            # response = 'This section is not function and for example only'
            

    # Send Response
    con.rtm_send_message(channel, response)  

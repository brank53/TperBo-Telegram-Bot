import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import urllib2
import requests
import pandas as pd
from tinytag import TinyTag
from telegram import Bot
from google.cloud import speech
from google.cloud import storage
from google.cloud.speech import enums
from google.cloud.speech import types
import time

def requestHttp(txt):
	request = 'https://hellobuswsweb.tper.it//web-services/hello-bus.asmx/QueryHellobus4ivr?fermata=' + txt + '&linea=&oraHHMM='
	r = requests.get(request)
	result = r.content
	tree = ET.ElementTree(ET.fromstring(result))
	return tree
	
def handling(res):
	temp = ""

	for i in res.iter():
		temp = i.text
		
	temp = temp.replace("\n", " ")
	temp = temp[16:]
	temp_ = temp.split(",")
	
	first = temp_[0]
	value = temp_[1]
	second = ""
	if "PEDANA" in value:
		ind = value.index("PEDANA")
		second = value[1:ind+7]
	else:
		ind = value.index(":")
		second = value[1:ind+3]
		
	return first, second

        
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    print content_type
    print chat_type
    print chat_id
    print msg
    
    """
    file_id = msg['voice']['file_id']
    newFile = Bot.get_file(file_id)
    newFile.download('voice.ogg')
    """
    file_name = msg['voice']['file_id']
    bot.download_file(msg['voice']['file_id'],"test_audio.ogg".format(file_name))
    
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        
        #res = requestHttp(txt)
        #first, second = handling(res)
        
        #bot.sendMessage(chat_id, first)
        #bot.sendMessage(chat_id, second)
        
        """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='IP', callback_data='ip'),
                     InlineKeyboardButton(text='Info', callback_data='info'),
                     InlineKeyboardButton(text='Time', callback_data='time')], 
                 ])
        bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
        """
        
        """
        stringList = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}
        
        inline_array = []
        for key, value in stringList.items():
			inline_array.append(InlineKeyboardButton(text=key, callback_data=value))

        keyboard_elements = [[element] for element in inline_array]

        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_elements )
		
        bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
        """
       
def on_callback_query(msg):
	query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, chat_id, query_data)

TOKEN = 'your_token'

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message, 'callback_query': on_callback_query})

print 'Listening ...'

while 1:
    time.sleep(10)


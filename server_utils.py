
from automated_gui import *
import requests
import os

TOKEN = os.getenv('TOKEN')

def parse_message(message):
    print("message-->",message)
    
    chat_id = message['message']['chat']['id']
    
    txt = message['message']['text']
    
    print("chat_id-->", chat_id)
    
    print("txt-->", txt)
    
    return chat_id,txt


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
def send_image(chat_id,path):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id='
    files = {'photo': open(path,'rb')}
    payload = {
        'chat_id': chat_id,
        'image': files,
        'caption': "This is a sample image"
    } 
    r = requests.post(url+ str(payload['chat_id']), files=files)
    return r 
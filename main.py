from flask import Flask
from flask import request
from flask import Response
from automated_gui import *
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
password = os.getenv('password')


app = Flask(__name__)
def parse_message(message):
    print("message-->",message)
    
    chat_id = message['message']['chat']['id']
    
    txt = message['message']['text']
    
    print("chat_id-->", chat_id)
    
    print("txt-->", txt)
    
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
def tel_send_image(chat_id,path):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id='
    files = {'photo': open(path,'rb')}
    payload = {
        'chat_id': chat_id,
        'image': files,
        'caption': "This is a sample image"
    }
    
    r = requests.post(url+ str(payload['chat_id']), files=files)
    return r
 
 
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    global validated
    
    if request.method == 'POST':
        msg = request.get_json()
        chat_id,txt = parse_message(msg)
        if validated:
            if txt == "take ss":
                path = take_screenshot()
                tel_send_image(chat_id,path)
            else:
                 tel_send_message(chat_id,'invalid command')
        else:
            if txt == password:
                validated = True
                tel_send_message(chat_id,'Welcome back')
            else:
                tel_send_message(chat_id,'Invalid password')
                
                
            
        
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


 
if __name__ == '__main__':  
    global validated
    validated = False
    app.run(debug=True)
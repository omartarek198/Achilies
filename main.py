from flask import Flask
from flask import request
from flask import Response
import os
from automated_gui import *
from server_utils import *
from dotenv import load_dotenv

load_dotenv()

password = os.getenv('password')


app = Flask(__name__)

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
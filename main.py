from flask import Flask
from flask import request
from flask import Response
import os
from automated_gui import *
from server_utils import *
from dotenv import load_dotenv
from commands import *

load_dotenv()

password = os.getenv('password')


app = Flask(__name__)


def find_input_command(txt):
    global list_Of_Commands
    for command in list_Of_Commands:
        if command.is_Command(txt):
            return command
    return None

def process_command(txt,chat_id):
    command = find_input_command(txt=txt)
    if command is not None:
        command.execute(chat_id)
    else:
         send_message(chat_id,'I cannot understand, use $list for my commands')
         
    
def validate(txt):
    if txt == password:
        return True
    else: return False

def post():
    global validated
    msg = request.get_json()
    chat_id,txt = parse_message(msg)
    if validated:
        process_command(txt=txt,chat_id=chat_id)
    elif validate(txt):  
        send_message(chat_id,'Welcome back')
        validated = True
    elif validate(txt) == False:
        send_message(chat_id,'Enter password')
    return Response('ok', status=200)



@app.route('/', methods=['GET', 'POST'])
def index():
    print( "index")
    if request.method == 'POST':
        return post()
       
    else:
        return "<h1>Welcome!</h1>"



def build_commands():
    obj = ScreenshotCommand("$ss")
    obj2 = Launch("$launch")
    obj3 = GoTo("$goto:whatsapp")
    commands = []
    commands.append(obj)
    commands.append(obj2)
    commands.append(obj3)
    
    return commands
 
if __name__ == '__main__':  
    global validated
    validated = False
    
    global list_Of_Commands
    list_Of_Commands = build_commands()
    app.run(debug=True)
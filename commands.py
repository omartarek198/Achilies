from server_utils import *
from command_class import CommandClass
from automated_gui import take_screenshot
from seli import * 

class ScreenshotCommand(CommandClass):
    def __init__(self, command_text):
        super().__init__(command_text)
    def execute(self,chatid):
        path =take_screenshot()
        send_image(chat_id= chatid,path=path)
        
class Launch(CommandClass):
    def __init__(self, command_text):
        super().__init__(command_text)
    def execute(self,chatid):
        launch_chrome()
class GoTo(CommandClass):
    def __init__(self, command_text):
        super().__init__(command_text)
    def execute(self,chatid):
        NavigateTo()
        
        
         
    

 
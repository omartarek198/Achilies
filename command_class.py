class CommandClass:
    def __init__(self, command_text):
        self.text = command_text
    def is_Command(self,text):
        if text == self.text:return True
        else: return False
    def display_command(self):
        print(self.text)
    def execute(self):
        pass
        
        
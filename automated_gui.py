
import pyautogui

def take_screenshot(path=""):
    #input (optional) : save path
    #return : screenshot path
    if path == "":
        path = 'screenshot.png'
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(path)
    return path

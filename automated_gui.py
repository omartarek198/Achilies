
import pyautogui

def take_screenshot(path=""):
    
    if path == "":
        path = 'screenshot.png'
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(path)
    return path

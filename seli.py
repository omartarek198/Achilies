from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options




 
 
def launch_chrome():
    

    
    import subprocess

    command1 = subprocess.Popen("python launch.py")
    
    
    print("done")
def NavigateTo():
    chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://web.whatsapp.com')
    x=[]
    print("done")
    


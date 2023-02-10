import os
import openai
from dotenv import load_dotenv
import requests
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


url = f'https://api.openai.com/v1/completions'
headers = {'Content-Type': 'application/json', 'Authorization': "Bearer "+ os.getenv("OPENAI_API_KEY")}
payload = {
  "model": "text-davinci-003",
  "prompt": "Say this is a test",
  "max_tokens": 7,
  "temperature": 0,
  "top_p": 1,
  "n": 1,
  "stream": False,
  "logprobs": None,
  "stop": "\n"
}


   
response = requests.post(url,json=payload,headers=headers)

for r in response:
    print(r)


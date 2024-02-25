import requests
import json

# flask api endpoint
url = 'http://127.0.0.1:5000/detect_sarcasm'

# test string
text = "This is a sarcastic text."

# payload for the POST request
payload = {'text': text}

# send POST request 
response = requests.post(url, json=payload)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)

import requests
import json

text = "my name is jason"

headers = {'accept': 'application/json'}
params = {"text": text}


response = requests.post('http://localhost:9000/languagedetection', headers=headers, params=params)
response_text = json.loads(response.text)

print("status code: {}".format(response.status_code))
print("response:    {}".format(response_text))
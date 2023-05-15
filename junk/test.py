import requests

files = {'file': open('test2.png','rb')}
#values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

r = requests.post("http://localhost:5000/api/v3?type=img", files=files)
print(r.text)
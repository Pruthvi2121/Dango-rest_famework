import requests
import json

url='http://127.0.0.1:8000/student/'
data ={
    'name':'Shraddha',
    'roll':1,
    'city':'Kolhapur',
}
json_data= json.dumps(data)

res = requests.post(url=url,data=json_data)
data = res.json()
print(data)
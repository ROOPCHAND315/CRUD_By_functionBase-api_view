import requests
import json

URL="http://127.0.0.1:8000/studentapi/"
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url = URL,headers=headers ,data = json_data)
    data = r.json()
    print(data)
# get_data()

def post_data():
    data={
        'name':'amit',
        'roll':105,
        'city':'Noida'
    }
    json_data=json.dumps(data)
    headers = {'content-Type':'application/json'}
    r=requests.post(url = URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# post_data()    

def put_data():
    data={
        'id':3,
        'name':'rohan',
        'roll':106,
        'city':'akbarpur'
    }
    json_data=json.dumps(data)
    headers = {'content-Type':'application/json'}
    r=requests.put(url = URL ,headers=headers,data=json_data)
    data=r.json()
    print(data)
# put_data()   

def delete_data():
    data={'id':4}
    json_data=json.dumps(data)
    headers = {'content-Type':'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
delete_data()    

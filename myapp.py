
import requests
import json

URL = "http://127.0.0.1:8000/Custapi/"


def create_data():
    data = {
        'name' : 'Anil',
        'mob' : 992274642
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

create_data()



def update_data():
    data = {
        'id' : 5,
        'branch' : 'pimpri',   #THE data i want to update 
    }

    json_data = json.dumps(data)   # converted from python to json
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)          

#update_data()


def delete_data():
    data = {
        'id' : 2
    }

    json_data = json.dumps(data)   # converted from python to json
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)          

#delete_data()


"""
def get_data():
    url = "http://127.0.0.1:8000/accc/"
    resp = requests.get(url)
    print(resp.json())
#get_data()
"""


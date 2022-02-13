import json
import requests
import json

URL=""
'''
If we give an Id to this function, we get data for that particular Id
If we dont, then we get data for all users
'''
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}# This id now goes from client to server
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

get_data(1)
import pandas as pd 
import json


#json格式更改
#data=pd.read_json('591DB_2.json')
#data['Id'] = data['Id'].astype(str)

#data.to_json('DB591_32.json',orient ='records',force_ascii =False)


with open('DB591_32.json','r') as fr:
    data = json.load(fr)


from pymongo import MongoClient
client = MongoClient()
db = client.DB591_2
coll = db.rent

coll.insert_many(data)
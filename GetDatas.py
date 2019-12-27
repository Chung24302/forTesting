#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import json


#json格式更改
data=pd.read_json('DB591_22.json')
data['Id'] = data['Id'].astype(str)


#get PhoneNumbers
data2 = pd.DataFrame(data['phoneNumber'])
data2['count'] = 1
result = data2.groupby('phoneNumber')['count'].sum().sort_values(ascending=False)

df = pd.DataFrame(result.index,columns=['phoneNumber'])
df.to_json('phoneQuery.json',orient ='records',force_ascii =False)

#get 屋主是吳小姐
data3 = data[data['lastName']=='吳小姐']
data3 = data[data['houseOwner']=='屋主']
data3 = data[data['region']=='TP']
data3.to_json('QueryMissWuAtTp.json',orient ='records',force_ascii =False)



#取得非屋主物件
data4 = data[data['houseOwner'].isin(['代理','仲介',''])]
data4.data3.to_json('QueryAgent.json',orient ='records',force_ascii =False)



#男生可租且在新北
data6 = data[data['region']=='NTP']
data8 = data6[data['gender'].isin(['男女生皆可','男生',''])]
data8.to_json('BoyRentQuery.json',orient ='records',force_ascii =False)




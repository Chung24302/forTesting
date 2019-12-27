import requests
import re
from bs4 import BeautifulSoup
import time
import pandas as pd

fileName = ['NTP','TP']

IdList =[]
houseOwnerList =[]
lastNameList =[]
phoneNumberList =[]
houseTypeList =[]
house_InfoList =[]
genderList =[]
regionList = []



for fn in fileName:
    id_data = pd.read_csv(fn+'_id.csv)
    
    for data in id_data['ID'][0:10]:
        
        res = requests.get(r'https://rent.591.com.tw/rent-detail-'+str(data)+'.html')
        time.sleep(3)
        soup = BeautifulSoup(res.text,'html.parser')

        #屋主姓氏
        try :
            lastName = soup.findAll('div',attrs={'style':'margin-top: 13px;'}) [0].text
            lastName = re.sub(pattern='[^\u4e00-\u9fa5]',repl='',string=str(lastName))[0:5]

            houseOwner = lastName[3:]
            lastName = lastName[0:3]
            
        except IndexError:
            print(data)
            #仲介姓氏
            ma = soup.findAll('div',{'class':'avatarRight'})
            for ddiv in ma:
                if '<i>' in str(ddiv) :
                    lastName=re.sub(pattern='[^\u4e00-\u9fa5]',repl='',string=str(ddiv))[0:5]

            houseOwner = lastName[3:]
            lastName = lastName[0:3]
         
        finally:
            #房子型態及現況

            houseType=''
            house_Info =[]
            for ultag in soup.findAll('ul',{'class':'attr'}):
                for litag in ultag.find_all('li'):
                    house_Info.append(litag.text)

            houseType = re.sub(pattern='[^\u4e00-\u9fa5]',repl='',string=house_Info[-2])[2:]
            house_Info = re.sub(pattern='[^\u4e00-\u9fa5]',repl='',string=house_Info[-1])[2:]

            #電話號碼

            phoneNumber = str(soup.findAll('span',{'class':'dialPhoneNum'}))
            phoneNumber = re.sub(pattern='[^0-9^-]',repl='',string=phoneNumber)[1:]

            #性別限制

            gender = ''
            for litag in soup.find_all('div',{'class':'two'}):
                for  tit in litag.find_all('em'):
                    if ('男' in tit.text) or ('女' in tit.text) :
                        gender=tit.text
            regionList.append(fn)
                        
        IdList.append(data)
        houseOwnerList.append(houseOwner)
        lastNameList.append(lastName)
        phoneNumberList.append(phoneNumber)
        houseTypeList.append(houseType)
        house_InfoList.append(house_Info)
        genderList.append(gender)

                          
                          
Totaldata ={
    'Id': IdList,
    'houseOwner': houseOwnerList,
    'lastName': lastNameList,
    'phoneNumber': phoneNumberList,
    'houseType': houseTypeList,
    'house_Info': house_InfoList,
    'gender': genderList,
    'region':regionList
}
df = pd.DataFrame(Totaldata)
df.to_json('test.json',orient ='records',force_ascii =False)
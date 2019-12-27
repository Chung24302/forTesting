import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



url = 'https://rent.591.com.tw/'


#  urlJumpIp 台北= 1 ，新北=3
rgNumber = ['1','3']
for rgn in rgNumber:
    driver = webdriver.Firefox()
    cookies = dict(urlJumpIp=rgn)
    res = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(res.text,'html.parser')

    path = '/html/body/div[2]/section[5]/div/div[1]/div[3]/div[1]/i'

    selector=etree.HTML(res.text) #將源碼轉化為能被XPath匹配的格式
    getMaxData = selector.xpath(path)
    maxData = int(getMaxData[0].xpath('string(.)').strip().replace(',','')) #取得最大筆數計算出最後一頁


    #取得所有單一頁面的連結代號
    for a in soup.select('h3 >a'):
        tmp = (re.sub(pattern='[^0-9^-]',repl='',string=str(a['href']))).replace('591--','')
        herp.append(tmp)
        
    df = pd.DataFrame(herp,columns=['ID'])
    if rgn == '1':
        df.to_csv('TP_id.csv',encoding = 'utd8')
    else:
        df.to_csv('NTP_id.csv',encoding = 'utd8')
import re
from selenium import webdriver
import json
import pandas as pd
import requests
# options = webdriver.ChromeOptions()
# options.binary_location = r"C:\Users\gsx\AppData\Local\Google\Chrome\Application\chrome.exe"
# driver_path=r'D:\python\chromedriver.exe'
# browser = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
# browser.get('https://mobile.yangkeduo.com/classification.html')
with open('data.txt',"r") as f:    #设置文件对象
     page_source = f.read()

str_json=re.search('<script id="__NEXT_DATA__" type="application/json" crossorigin="anonymous">(.*?)</script>',page_source)
rootData=json.loads(str_json.group(1))['props']['pageProps']['data']['operationsData']['rootData']
print(rootData[0])
dataList=[]
for d in rootData:
    datadict={'optID':0,'optType':1,'optName':'','fid':0,'imgUrl':'','linkUrl':'wu'}
    datadict['optID']=d['optID']
    datadict['optName']=d['optName']
    dataList.append(datadict)
    for i in d['cat']:
        newdatadict = {'optID': 0, 'optType': 2, 'optName': '', 'fid': 0, 'imgUrl': '','linkUrl':''}
        newdatadict['optID']=i['optID']
        newdatadict['fid']=d['optID']
        newdatadict['optName']=i['optName']
        newdatadict['imgUrl']=i['imgUrl']
        newdatadict['linkUrl']=i['linkUrl']
        dataList.append(newdatadict)
data=pd.DataFrame(dataList)
data.to_csv('data.csv',index=False)
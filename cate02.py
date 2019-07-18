import pandas as pd
from selenium import webdriver
import requests
import json
import re
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '123456', '127.0.0.1:3306', 'mysql'))
con = engine.connect()#创建连接
data=pd.read_csv('data.csv')
n=0
headers={
'cookie': 'api_uid=rBRc/V0rAJpMn1SlDR1tAg==; ua=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F75.0.3770.100%20Safari%2F537.36; _nano_fp=XpdjXq9blpPbX0EbnT_rkyIj~ZssRna0y8u4kwSu; webp=1; pdd_user_uin=IYNYCIGNBCRX7CI7NUGK6ADGHU_GEXDA; rec_list_index=rec_list_index_8ZIswo; JSESSIONID=CE639C97A00BFF6AC38E82D5F7F90E94; pdd_user_id=2639042956778; PDDAccessToken=72IFVHEJO2C5S4RHCIEKTZVEKBC2UINQ5UGUM673EIBIC3T7APLQ101eaad',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
newlist=[]
for i in range(len(data)):
    s=data.iloc[i]
    if 'catgoods.html' in s['linkUrl']:
        url = 'https://mobile.yangkeduo.com/catgoods.html?opt_id={}&opt_g=1&opt_type=2'.format(s['optID'])
        html=requests.get(url,headers=headers)
        print(html.status_code)
        with open('data2.txt', "w",encoding='utf-8') as f:  # 设置文件对象
            f.write(html.text)
        with open('data2.txt', "r",encoding='utf-8') as f:  # 设置文件对象
            page_source = f.read()
        str_json = re.search('type="application/json" crossorigin="anonymous">(.*?)</script>',
                             page_source)
        rootData = json.loads(str_json.group(1))['props']['pageProps']['data']['optsInfo']
        print(rootData[0])
        dataList=[]
        for d in rootData:
            datadict={'optID':0,'optType':3,'optName':'','fid':0,'imgUrl':''}
            datadict['optID']=d['optID']
            datadict['optName']=d['optName']
            datadict['fid']=s['optID']
            dataList.append(datadict)
        newlist=newlist+dataList
newdata=pd.DataFrame(newlist)
newdata.to_csv('data01.csv',index=False)

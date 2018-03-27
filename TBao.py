import re,time,requests, pandas

ren = re.compile(r'"pic_url":"(.*?)"')
#代替浏览器发送请求的头部信息
head = {'user-agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'}

for n in range (1,2):
    url ='https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&psort=_lw_quantity&s='+str(44*(n-1))
    html = requests.get(url)
    data = re.findall(ren,html.text)
    data2 = pandas.DataFrame(data)
    data2.to_csv('D:\\pyCharmProjects\\Crawlers\\Tb.csv',header= False,index= False,mode='a+')

import pandas as pd
from lxml import etree
import re
import os
import requests

def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html=requests.get(url,headers=headers)
    print(html.status_code)
    html.encoding=html.apparent_encoding
    return html.text
# 文学 流行 文化 生活 经管 科技
def parse_html(html):
    Types=[]
    # // *[ @ id = "content"] / div / div[1] / div[2]
    # //*[@id="content"]/div/div[1]/div[2]/div[1]
    # //*[@id="content"]/div/div[1]/div[2]
    # //*[@id="content"]/div/div[1]/div[2]
    html = etree.HTML(html)
    # divs=html.xpath('//div[@class="article"]/div[2]/div')
    divs = html.xpath('//div[@class="article"]/div[2]/div')
    print(len(divs))
    for div in divs:
        type0=div.xpath('.//a[@class="tag-title-wrapper"]/@name')[0]
        tds=div.xpath('.//td')
        for td in tds:
            name=td.xpath('.//a/text()')[0]
            num=td.xpath('.//b/text()')[0]
            num=Num(num)
            bt={'type0':type0,'name':name,'num':num}
            Types.append(bt)
    return Types


def Num(info):
    r = re.findall(r'[\(](.*?)[\)]', info)[0]
    return int(r)


def run():
    if 'bookType.csv' not in os.listdir():
        url = 'https://book.douban.com/tag/'
        html = get_html(url)
        Types = parse_html(html)
        typedf=pd.DataFrame(Types)
        typedf.to_csv('bookType.csv')
    else:
        typedf = pd.read_csv('bookType.csv',encoding='utf_8_sig')
    return typedf


if __name__ == '__main__':
    run()
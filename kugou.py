import requests
from lxml import etree
import re
import wordcloud
import imageio
import pandas as pd



def get_html(url):
    headers = {
    'User-Agen': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    html=requests.get(url,headers=headers)
    html.encoding=html.apparent_encoding
    return html.text


def parse_html(html):
    html=etree.HTML(html)
    lis=html.xpath('//div[@class="pc_temp_songlist "]/ul/li')
    names=[]
    sings=[]
    for li in lis:
        title=li.xpath('@title')[0].strip()
        title=title.split("-")
        name=title[1].strip()
        name=re.sub(u'\\(.*?\\)','',name).strip()
        names.append(name)
        sing={'singer':title[0].strip(),'sing_name':name}
        sings.append(sing)
    singStr=','.join(names)
    return singStr,sings


def world(s):
    mk = imageio.imread("yuan.png")
    w = wordcloud.WordCloud(width=1000, height=1200, background_color='white',
                        mask=mk,font_path='msyh.ttc')
    w.generate(s)
    w.to_file('歌名.png')


if __name__ == '__main__':
    singnames=[]
    singdf = pd.DataFrame()
    # 如果想读取全部的需要将此处的4改成25
    for i in range(1,4):
        url='https://www.kugou.com/yy/rank/home/%d-8888.html?from=rank'%(i)
        html=get_html(url)
        t=parse_html(html)
        singStr=t[0]
        sings=t[1]
        singnames.append(singStr)
        singdf1 = pd.DataFrame(sings)
        singdf = pd.concat([singdf, singdf1], axis=0, ignore_index=True)
    singdf.to_csv('sings.csv',encoding='utf_8_sig',index=False)
    singAllname=','.join(singnames)
    world(singAllname)



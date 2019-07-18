from lxml import etree
import requests
import pandas as pd
import os
import re


def get_html(url):
    '''
    根据url获得网页内容
    :param url:
    :return:
    '''
    headers={'User-Agen':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html=requests.get(url,headers=headers)
    print(html.status_code)
    html.encoding=html.apparent_encoding
    return html.text


def parse_html(html):
    '''
    使用lxml模块xpath技术对网页
    :param html:
    :return:
    '''
    books=[]
    html=etree.HTML(html)
    tables=html.xpath('//div[@class="indent"]/table')
    print(len(tables))
    for table in tables:
        name=table.xpath('.//div[@class="pl2"]/a/@title')[0]
        info=table.xpath('.//p[@class="pl"]/text()')[0]
        year=Year(info)
        introduce=table.xpath('.//span[@class="inq"]/text()')
        if len(introduce)==0:
            introduce='无'
        else:
            introduce=introduce[0]
        nation=Nation(info)
        book={'name':name,'info':info,'nation':nation,'introduce':introduce,'year':year}
        books.append(book)
    return books


def Nation(info):
    '''
    选取其中的info信息
    :param info:
    :return:
    '''
    if ']' in info:
        r = re.findall(r'[\[](.*?)[\]]', info)[0]
    else:
        r='中'
    return r


def Year(info):
    '''
    选取其中的年份信息
    :param info:
    :return:
    '''
    r=re.findall(r'\d{4}',info)[0]
    return r


def run():
    '''
    运行主函数
    :return:
    '''
    if 'bookTop250.csv' not in os.listdir():
        bookdf = pd.DataFrame()  # 存储生成的movie dataframe
        for i in range(10):  # 需要循环10次请求页面
            s = i * 25
            # 使用python占位符
            url = 'https://book.douban.com/top250?start=%d' % (s)
            html = get_html(url)
            books = parse_html(html)
            bookdf1 = pd.DataFrame(books)
            bookdf = pd.concat([bookdf, bookdf1], axis=0, ignore_index=True)
        bookdf.to_csv('bookTop250.csv', index=False)
    else:
        bookdf=pd.read_csv('bookTop250.csv',encoding='utf_8_sig')
    return bookdf


if __name__ == '__main__':
    run()
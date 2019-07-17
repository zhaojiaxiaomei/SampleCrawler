from lxml import etree
import requests
import pandas as pd
import os
import matplotlib.pyplot as plt
import random

# 20177710513韩田慧
def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    html=requests.get(url,headers=headers)
    print(html.status_code)
    html.encoding=html.apparent_encoding
    return html.text


def parse_html(html):
    movies=[]
    imglist=[]
    html=etree.HTML(html)
    lis=html.xpath('//ol[@class="grid_view"]/li')
    for li in lis:
        name=li.xpath('.//a/span[@class="title"]/text()')[0]
        director_actor=li.xpath('.//div[@class="bd"]/p/text()')[0].strip()
        info=li.xpath('.//div[@class="bd"]/p/text()')[1].strip()
        info=clinfo(info)
        rating_score=li.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()')[0]
        rating_num = li.xpath('.//div[@class="star"]/span[4]/text()')[0]
        introduce=li.xpath('.//p[@class="quote"]/span/text()')[0]
        imgurl=li.xpath('.//img/@src')[0]
        movie={'name':name,'director_actor':director_actor,'info':info
               ,'rating_score':rating_score,'rating_num':rating_num
               ,'introduce':introduce,'imgurl':imgurl}
        movies.append(movie)
        imglist.append(imgurl)
    return movies,imglist


def clinfo(s):
    if '中国' in s:
        s=s+'中国大陆'
    elif '香港' in s:
        s = s
    elif '美国' in s:
        s = s
    elif '日本' in s:
        s = s
    elif '英国' in s:
        s = s
    else:
        s = s + '其他'
    return s


def downloding(url,xh):
    if 'moviePoster' in os.listdir():
        pass
    else:
        os.mkdir('moviePoster')
    os.chdir(r'.\moviePoster')
    img=requests.get(url,timeout=1.5).content
    with open(str(xh)+'.png','wb') as f:
        f.write(img)


def printYear(moviedf):
    yearList=[]
    result=[['1930s',0],['1940s',0],['1950s',0]
        , ['1960s', 0],['1970s', 0],['1980s', 0]
            ,['1990s', 0],['2000s', 0],['2010s', 0]]
    for s in moviedf['info']:
        s="".join(s.split()).split('/')
        yearList.append(s[0][:4])
    yearl=list(set(yearList))
    for i in yearl:
        n=0
        for j in yearList:
            if i==j:
                n+=1
        if int(i)<1940:
            result[0][1]+=n
        elif int(i)>=1940 and int(i)<1950:
            result[1][1] += n
        elif int(i)>=1950 and int(i)<1960:
            result[2][1] += n
        elif int(i) >= 1960 and int(i) < 1970:
            result[3][1] += n
        elif int(i) >= 1970 and int(i) < 1980:
            result[4][1] += n
        elif int(i) >= 1980 and int(i) < 1990:
            result[5][1] += n
        elif int(i) >= 1990 and int(i) < 2000:
            result[6][1] += n
        elif int(i) >= 2000 and int(i) < 2010:
            result[7][1] += n
        else:
            result[8][1] += n
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.bar([i for i in range(len(result))], [i[1] for i in result], width=0.3)
    for i in range(len(result)):
        plt.text(i - 0.1, result[i][1] + 0.3, result[i][1])
    plt.xticks([i for i in range(len(result))], [i[0] for i in result], rotation=1)
    plt.title('经典电影每个年代电影数量')
    plt.ylabel('数量')
    # plt.annotate(r'$author:20177710513韩田慧', (0, 60), color='#C4C4C4')
    plt.savefig('year.png')
    plt.show()

def run():
    moviedf = pd.DataFrame() # 存储生成的movie dataframe
    for i in range(10): #需要循环10次请求页面
        s = i * 25
        # 使用python占位符
        url = 'https://movie.douban.com/top250?start=%d&filter=' % (s)
        html = get_html(url)
        movies = parse_html(html)
        movdf = pd.DataFrame(movies[0])
        moviedf = pd.concat([moviedf, movdf], axis=0, ignore_index=True)

    moviedf.to_csv('movieTop250.csv', index=False)
    printYear(moviedf)
    return moviedf


def Selectcountry(s,moviedf):
    movielist=[]
    for i in range(len(moviedf)):
        if s in moviedf.loc[i]['info']:
            movielist.append(["《"+str(moviedf.loc[i]['name'])+"》--------------",str(moviedf.loc[i]['introduce'])])
    return movielist


def randomMovie(moiedf):
    xh = random.randint(0, 249)
    movie=dict(moiedf.loc[xh])
    downloding(url=movie['imgurl'],xh=xh)
    os.chdir(r'..')
    return movie,xh


if __name__ == '__main__':
    f = open('movieTop250.csv', encoding='UTF-8')
    df = pd.read_csv(f)
    # Selectcountry('其他',df)
    printYear(df)
    #run()




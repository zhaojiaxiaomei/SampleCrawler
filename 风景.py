import requests
from bs4 import BeautifulSoup
import os
url='http://www.win4000.com/zt/fengjing_1.html'
headers = {
        'User-Agen': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')
div = soup.find_all(class_="tab_box")[0]
ul = div.find(class_="clearfix")
alist = ul.find_all('a')
a_href = []
if 'images' in os.listdir():
    pass
else:
    os.mkdir('images')
for i in range(len(alist)):
    img = alist[i].find('img')
    os.chdir(r'.\images')
    img = requests.get(img['data-original'], timeout=1.5).content
    with open(str(i+1)+'汪成'+'.png', 'wb') as f:
        f.write(img)
    os.chdir(r'..')


# http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid={}
import requests
import re
keyword=input('请输入你想要下载的音乐：')
class MusicSpider(object):
    def __init__(self):
        self.url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid={}'
        self.get_id_url='http://music.taihe.com/search?key={}'.format(keyword)

    def get_id(self,url):
        req=requests.get(url).text
        reg=re.compile('data-songdata=\'{ "id": "(.*?)" }')
        music_id=re.findall(reg,req)[0]
        return music_id

    def get_music_url(self):
        music_id=self.get_id(self.get_id_url)
        req=requests.get(self.url.format(music_id)).json()
        return req['bitrate']['show_link']

    def run(self):
        url=self.get_music_url()
        req=requests.get(url).content
        with open(keyword+'.mp3','wb') as f:
            f.write(req)


if __name__ == '__main__':
    spider=MusicSpider()
    spider.run()
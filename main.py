import requests
from bs4 import BeautifulSoup
import os
path='./豆瓣'
if __name__ == '__main__':
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'referer': 'https: // pagead2.googlesyndication.com /'
    }
    url = 'https://movie.douban.com/top250'
    #获取整个网页源码
    page_data = requests.get(url=url,headers=headers).text
    #煲汤实例化对象
    soup = BeautifulSoup(page_data,'lxml')
    #寻找各个电影封面
    movies = len(soup.select('#wrapper .grid_view > li img'))
    #创建程序所在文件夹
    if not os.path.isdir(path):
        os.mkdir(path)
    #将工作目录改为刚创建的文件夹里
    os.chdir(path)
    #收集每部电影的封面
    for i in range(0,movies):
        #每个电影名称
        img_name = soup.select('#wrapper .grid_view > li img')[i]['alt']
        path_img = os.getcwd() + '/' + str(i+1) + img_name + '.jpg'
        #电影图片
        url_img_movie = soup.select('#wrapper .grid_view > li img')[i]['src']
        header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'sec - ch - ua - mobile': '?0',
            'sec - ch - ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"'
        }
        #获取图片数据并以二进制保存在img_movie里
        img_movie = requests.get(url=url_img_movie,headers=header).content
        #存储
        with open(path_img,'wb') as fp:
            fp.write(img_movie)
        print(img_name+'已下载完成!')

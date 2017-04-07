# -*- coding: utf-8 -*-
__author__ = 'PatchLion'

from bs4 import BeautifulSoup
import requests
import os

def loadUrl(url):
    html = requests.request("GET", url)
    print(html.content)
    soup = BeautifulSoup(html.content, 'lxml')
    list = soup.find_all('img')
    #img_list = []
    rootpath = "image"
    if not os.path.exists(rootpath):
        os.mkdir(rootpath)
    index = 0
    for value in list:
        #img_list.append(value['src'])
        downloadImg(value['src'], os.path.join(rootpath, str(index) + ".jpg"))
        index += 1

def downloadImg(url, savepath):
    data = requests.request('GET', url)
    with open(savepath, 'wb') as f:
        f.write(data.content)

loadUrl("http://tieba.baidu.com/p/2166231880")
#提取章节url

import requests

from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        htmlText = r.text
        return htmlText
    except:
        return "getHTMLText产生异常"


def getTagList(htmlText):
    soup = BeautifulSoup(htmlText,'html.parser')
    tagList = soup.find_all('a',href=re.compile('(\d)*.html'))[1:]
    return tagList

def getUrlList(tagList):
    urlList = list.copy(tagList)
    urlLen = len(tagList)
    for i in tagList:
        urlList[urlLen-1] = i.get('href')
        urlLen = urlLen - 1
    urlList.reverse()   # reverse list  item
    return urlList

if __name__== "__main__":
    url = "http://www.biquge.com.tw/0_278/"
    
    htmlText = getHTMLText(url)
    tagList = getTagList(htmlText)
    urlList = getUrlList(tagList)

    for i in urlList:
        print(i)

#复制的v4

#此版本任务:
#       输出文学作品名称

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

def completeUrl(url,road):
    return (url + road[1:])

def getContent(url):
    r = getHTMLText(url)
    soup = BeautifulSoup(r,'html.parser')
    content = soup.find_all(id='content')
    content = content[0].get_text()
    return content

def getTitle(htmlText):
    soup = BeautifulSoup(htmlText,'html.parser')
    title = soup.h1.get_text()
    return title


if __name__== "__main__":
    bqg_url = "http://www.biquge.com.tw/"
    url = "http://www.biquge.com.tw/0_278/"
    
    htmlText = getHTMLText(url)
    tagList = getTagList(htmlText)
    urlList = getUrlList(tagList)
    
    title = getTitle(htmlText)

    print(title)

    #for i in urlList:
        #reall_url = completeUrl(bqg_url,i)
        #content = getContent(reall_url)
        #file_name = "a.text"
        #f = open(file_name,"a")
        #f.write(content)
        #f.close()
        #print(content)
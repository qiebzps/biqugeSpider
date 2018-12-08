#更新自v9

#此版本任务:
#       将所有小说的Url添加到列表


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

def writeContent(fileName,title,content):
    f = open(fileName,"a")
    f.write(title)
    f.write(content[:-1])
    f.close()

def getTarget(targetUrl):
    htmlText = getHTMLText(url)
    tagList = getTagList(htmlText)
    urlList = getUrlList(tagList)
    file_name = getTitle(htmlText)+".txt"
    
    for i in urlList:
        reall_url = completeUrl(bqg_url,i)
        content = getContent(reall_url)
        title = "\n"+getTitle(getHTMLText(reall_url))+"\n"
        writeContent(file_name,title,content)

def getAllList(bqg_url):
    allList = []
    #####算法优化:
    #####   a_b
    #####   a等于b整除1000
    a = 0
    b = 0
    while(1 and b < 20298):#目前网站总共20297本作品
        bookNumber = str(a) + "_" + str(b)
        #print(bookNumber)
        realUrl = bqg_url + bookNumber + "/"
        allList.append(realUrl)
        b = b + 1
        a = b // 1000
    return allList

if __name__== "__main__":
    bqg_url = "http://www.biquge.com.tw/"
    url = "http://www.biquge.com.tw/0_278/"

    #getTarget(url)
    allList = getAllList(bqg_url)

    for i in allList:
        print(i)

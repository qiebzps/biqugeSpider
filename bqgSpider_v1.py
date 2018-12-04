#提取章节url

import requests

from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "getHTMLText产生异常"

if __name__== "__main__":
    url = "http://www.biquge.com.tw/0_278/"
    demo = getHTMLText(url)
    soup = BeautifulSoup(demo,'html.parser')
    #print(soup.prettify())
    #print(soup.find_all('dd')) #章节链接<a href=''>...</a>所在的标签
    #print(soup('dd'))
    #print(soup.dd.find_all('a'))

    #print(soup.find_all('a',href=re.compile('(\d)*.html')))

    # 提取章节url
    # 从下标为1的开始的原因是为了去重（查看网页结构即可知）
    for link in soup.find_all('a',href=re.compile('(\d)*.html'))[1:]:
        print(link.get('href'))


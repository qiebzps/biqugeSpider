# 爬取网页的通用代码框架

import requests

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
    print(getHTMLText(url))

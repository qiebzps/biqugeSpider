import bqgSpider_v0
from bs4 import BeautifulSoup

url = "https://baidu.com/"
demo = bqgSpider_v0.getHTMLText(url)
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())

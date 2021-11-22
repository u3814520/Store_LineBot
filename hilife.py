import  requests
from fake_useragent import UserAgent
import pandas as pd
import time
import json
from bs4 import BeautifulSoup

url = 'https://www.hilife.com.tw/storeInquiry_street.aspx'
userAgent = UserAgent().random
headers={'Referer': 'https://www.hilife.com.tw/storeInquiry_street.aspx','User-Agent':userAgent}
county={'CITY': '屏東縣','AREA': '萬丹鄉'}
res = requests.post(url,headers=headers)
# res = requests.post(url,data=county)
soup = BeautifulSoup(res.text, 'html.parser')
titles = soup.select('div[class="searchResults"]')
print(titles)
# for a in titles:
#     job = a.select('th')[1]
#     print(job)
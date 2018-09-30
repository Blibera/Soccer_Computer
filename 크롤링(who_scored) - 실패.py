from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import requests
import pymysql
import time
import re

# MySql 연결
conn = pymysql.connect(host='localhost', user='root', password='autoset', db='test', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# 모르겠음
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}

# url
url = 'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/6829/England-Premier-League'

# 변수정의
rc_count = 0

# 셀레니움 -> BeautifulSoup -> str 변환
driver = webdriver.Chrome('C:/chromedriver')
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
text = str(soup)

# 'result-1 rc' 개수 세기 (해당 수 만큼 루프 하기 위해서)
rc_count = text.count('result-1 rc')
print(rc_count)

# 35주 경기
for loop in range (0,35):
    for i in range (1,rc_count+1):
        # url_Second 추출
        url_second = text.split('result-1 rc')[i]
        url_second = url_second.split('href="')[1]
        url_second = url_second.split('"')[0]
        url_second = "https://www.whoscored.com" + url_second

        # 2차 url로 접속하여 세부정보 파싱
        response = requests.get(url_second, headers=headers)
        html = response.text
        text_second = str(html)

        Home = text_second.split('team-link')[1]
        Home = Home.split('">')[1]
        Home = Home.split('<')[0]
        Home = Home.strip()

        Away = text_second.split('team-link')[2]
        Away = Home.split('">')[1]
        Away = Home.split('<')[0]
        Away = Home.strip()

        print(Home)
        print(Away)

        time.sleep(100)

"""
# 다음페이지 넘어가기 XPath 이용 (참고 : https://wkdtjsgur100.github.io/selenium-xpath/)
driver.find_element_by_xpath("//div[@id='date-controller']/a[@class='previous button ui-state-default rc-l is-default']").click()
time.sleep(2)
"""

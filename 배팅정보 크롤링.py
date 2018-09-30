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

# 자동화용

a = ["2017-2018", "2016-2017", "2016-2017", "2015-2016", "2014-2015", "2013-2014", "2012-2013", "2011-2012", "2010-2011"]

def day_set(text):
    input_day = re.sub(' ','-',text)
    year = input_day.split('-')[2]
    month = input_day.split('-')[1]
    day = input_day.split('-')[0]

    if month=="January":
        month = "01"
    elif month=="February":
        month = "02"
    elif month=="March":
        month = "03"
    elif month=="April":
        month = "04"
    elif month=="May":
        month = "05"
    elif month=="June":
        month = "06"
    elif month=="July":
        month = "07"
    elif month=="August":
        month = "08"
    elif month=="September":
        month = "09"
    elif month=="October":
        month = "10"
    elif month=="November":
        month = "11"
    else:
        month = "12"

    if day == "1":
        day = "01"
    elif day == "2":
        day = "02"
    elif day == "3":
        day = "03"
    elif day == "4":
        day = "04"
    elif day == "5":
        day = "05"
    elif day == "6":
        day = "06"
    elif day == "7":
        day = "07"
    elif day == "8":
        day = "08"
    elif day == "9":
        day = "09"

    month = str(month)
    day = year+month+day
    return day

# 8번 루프하면 됨
for p in range (3,4):
    print("루프")
    for i in range (1,9):
        # 변수 초기화
        re_count = 0

        # url파싱
        driver = webdriver.Chrome('C:/chromedriver')
        url = "http://www.oddsportal.com/soccer/england/premier-league-" + str(a[p]) + "/results/#/page/" + str(i)

        # 셀레니움 -> BeautifulSoup -> str 변환
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        text = str(soup)

        # 날짜 분류
        day_count = html.count('center nob-border')

        for j in range(1, (day_count + 1)):
            # 경기 분류
            loop = text.split('table-dummyrow')[j]
            xeid_count = loop.count('xeid')

            # 날짜
            day = html.split('center nob-border">')[j]
            day = day.split('datet ')[1]
            day = day.split('">')[1]
            day = day.split('<')[0]
            day = day_set(day)

            for k in range(1, xeid_count + 1):
                match = loop.split('xeid')[k]

                try:
                    # 홈, 어웨이
                    home_away = match.split('name table-participant">')[1]
                    home_away = home_away.split('href="')[1]
                    home_away = home_away.split('</a>')[0]
                    home_away = re.sub('<span class="bold">', '', home_away)
                    home_away = re.sub('</span>', '', home_away)
                    home_away = home_away.split('">')[1]
                    home_away = home_away.strip()
                    home_name = home_away.split('-')[0]
                    home_name = home_name.strip()

                    away_name = home_away.split('-')[1]
                    away_name = away_name.strip()

                    # 배당
                    home_bet = match.split('xparam="odds_text">')[1]
                    home_bet = home_bet.split('<')[0]
                    home_bet = home_bet.strip()

                    draw_bet = match.split('xparam="odds_text">')[2]
                    draw_bet = draw_bet.split('<')[0]
                    draw_bet = draw_bet.strip()

                    away_bet = match.split('xparam="odds_text">')[3]
                    away_bet = away_bet.split('<')[0]
                    away_bet = away_bet.strip()
                    sql = "INSERT INTO bet (Day, Home_name, Away_name, Home_bet, Draw_bet, Away_bet) VALUES (%s,%s,%s,%s,%s,%s)"
                    curs.execute(sql, (
                    int(day), str(home_name), str(away_name), float(home_bet), float(draw_bet), float(away_bet)))
                    conn.commit()
                except:
                    pass

        driver.quit()
        time.sleep(2)
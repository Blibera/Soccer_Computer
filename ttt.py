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
user_agent = "'Mozilla/5.0"
headers = {"User-Agent": user_agent}

# url
url = ['https://us.soccerway.com/teams/england/huddersfield-town-fc/726/matches/','https://us.soccerway.com/teams/england/brighton--hove-albion-fc/703/matches/',\
       'https://us.soccerway.com/teams/england/stoke-city-fc/690/matches/','https://us.soccerway.com/teams/england/southampton-fc/670/matches/', \
       'https://us.soccerway.com/teams/wales/swansea-city-afc/738/matches/', 'https://us.soccerway.com/teams/england/crystal-palace-fc/679/matches/', \
       'https://us.soccerway.com/teams/england/afc-bournemouth/711/matches/', 'https://us.soccerway.com/teams/england/everton-football-club/674/matches/', \
       'https://us.soccerway.com/teams/england/watford-football-club/696/matches/', 'https://us.soccerway.com/teams/england/west-bromwich-albion-football-club/678/matches/']
name = ['Huddersfield Town','Brighton & Hove Albion','Stoke City','Southampton','Swansea City', \
        'Crystal Palace', 'AFC Bournemouth','West Ham United','Watford','West Bromwich Albion']

# 페이지 넘김

def url_clean(url):
    cleaned_text = re.sub('=', '', url)
    cleaned_text = re.sub('>', '', cleaned_text)
    cleaned_text = re.sub('\"', '', cleaned_text)
    cleaned_text = cleaned_text.lstrip()
    cleaned_text = cleaned_text.rstrip()
    return cleaned_text

def strip(text):
    text = text.lstrip()
    text = text.rstrip()
    return text

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

for k in range(8,10):
    driver = webdriver.Chrome('C:/chromedriver')
    driver.get(url[k])
    Select_name = name[k]

    for j in range(0,8):

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        text = str(soup)

        text = str(soup)

        Team = text.split('subheading')[1]
        Team = Team.split('<h1>')[1]
        Team = Team.split('</h1>')[0]
        Team = strip(Team)

        print(str(k) + "번째 팀 "+str(j) + "번째 시즌 루프중")
        for i in range(2,52):

                # 1초 텀주기
                time.sleep(1)

                # 초기화 변수들
                home_name = ""
                away_name = ""
                home = 0
                away = 0
                emeny_name = ""
                Home_play_1 = ""
                Home_play_2 = ""
                Home_play_Score = ""
                Ememy_1 = ""
                Ememy_2 = ""
                Ememy_Score = ""

                result=0

                # 해당 경기종류 추출(EPL,ICC,UCL)
                not_epl = text.split('data-timestamp')[i-1]
                not_epl = not_epl.split('title')[1]
                not_epl = not_epl.split('>')[1]
                not_epl = not_epl.split('<')[0]

                if not_epl=="PRL":
                    not_epl = int(1)
                else:
                    not_epl = int(0)

                # 경기 url 추출
                team = text.split('team-a')[i]
                url = team.split('score-time')[1]
                url = url.split('href')[1]
                url = url.split('>')[0]
                url = url_clean(url)
                url = "https://us.soccerway.com/" + url

                try:
                    # 파싱
                    response = requests.get(url, headers=headers)
                    html = response.text

                    # 홈 팀명
                    home_name = html.split('page_match_1_block_match_info_4-wrapper')[1]
                    home_name = home_name.split('href')[1]
                    home_name = home_name.split('>')[1]
                    home_name = home_name.split('<')[0]
                    home_name = strip(home_name)

                    # 어웨이 팀명
                    away_name = html.split('page_match_1_block_match_info_4-wrapper')[1]
                    away_name = away_name.split('container ')[3]
                    away_name = away_name.split('href')[1]
                    away_name = away_name.split('>')[1]
                    away_name = away_name.split('<')[0]

                    # 홈, 어웨이, 적팀이름 (이름 변경 필수!)
                    if (home_name == Select_name):
                        home = 1
                        emeny_name = away_name
                    else:
                        away = 1
                        emeny_name = home_name

                    # 날짜
                    day = html.split('page_match_1_block_match_info_4-wrapper')[1]
                    day = day.split('Competition')[1]
                    day = day.split('Date')[1]
                    day = day.split('href')[1]
                    day = day.split('>')[2]
                    day = day.split('<')[0]
                    day = day_set(day)

                    # 점수 추출
                    play = html.split('page_match_1_block_match_info_4-wrapper')[1]
                    play1 = play.split('Competition')[1]
                    play1 = play1.split('Date')[1]
                    play1 = play1.split('Half-time')[1]
                    play1 = play1.split('Full-time')[0]
                    play1 = play1.split('>')[2]
                    play1 = play1.split('<')[0]

                    play2 = play.split('Competition')[1]
                    play2 = play2.split('Date')[1]
                    play2 = play2.split('Full-time')[1]
                    play2 = play2.split('>')[2]
                    play2 = play2.split('<')[0]

                    play1 = re.sub(' ', '', play1)
                    play2 = re.sub(' ', '', play2)
                    Home_play1 = play1.split('-')[0]
                    Away_play1 = play1.split('-')[1]

                    Home_playScore = play2.split('-')[0]
                    Away_playScore = play2.split('-')[1]

                    Home_play1 = int(Home_play1)
                    Home_playScore = int(Home_playScore)

                    Away_play1 = int(Away_play1)
                    Away_playScore = int(Away_playScore)

                    Home_play2 = Home_playScore - Home_play1
                    Away_play2 = Away_playScore - Away_play1

                    if (home == 1):
                        Home_play_1 = Home_play1
                        Home_play_2 = Home_play2
                        Home_play_Score = Home_playScore
                        Ememy_1 = Away_play1
                        Ememy_2 = Away_play2
                        Ememy_Score = Away_playScore
                    else:
                        Ememy_1 = Home_play1
                        Ememy_2 = Home_play2
                        Ememy_Score = Home_playScore
                        Home_play_1 = Away_play1
                        Home_play_2 = Away_play2
                        Home_play_Score = Away_playScore

                    if Home_play_Score > Ememy_Score:
                        result = 2
                    elif Home_play_Score < Ememy_Score:
                        result = 0
                    else:
                        result = 1

                    Chart_url = html.split('General Game Stats Chart')[1]
                    Chart_url = Chart_url.split('src=')[1]
                    Chart_url = Chart_url.split('style')[0]
                    Chart_url = re.sub('\'', '', Chart_url)
                    Chart_url = "https://us.soccerway.com" + Chart_url

                    response_Chart = requests.get(Chart_url, headers=headers)
                    Chart_html = response_Chart.text

                    # 코너킥
                    Home_Play_Corner_me = Chart_html.split('legend left value')[1]
                    Home_Play_Corner_me = Home_Play_Corner_me.split('>')[1]
                    Home_Play_Corner_me = Home_Play_Corner_me.split('<')[0]

                    Home_Play_Corner_you = Chart_html.split('legend right value')[1]
                    Home_Play_Corner_you = Home_Play_Corner_you.split('>')[1]
                    Home_Play_Corner_you = Home_Play_Corner_you.split('<')[0]

                    Home_Play_Corner_me = int(Home_Play_Corner_me)
                    Home_Play_Corner_you = int(Home_Play_Corner_you)

                    # 슈팅
                    Home_Play_Shot_me = Chart_html.split('legend left value')[2]
                    Home_Play_Shot_me = Home_Play_Shot_me.split('>')[1]
                    Home_Play_Shot_me = Home_Play_Shot_me.split('<')[0]

                    Home_Play_Shot_you = Chart_html.split('legend right value')[2]
                    Home_Play_Shot_you = Home_Play_Shot_you.split('>')[1]
                    Home_Play_Shot_you = Home_Play_Shot_you.split('<')[0]

                    Home_Play_Shot_me = int(Home_Play_Shot_me)
                    Home_Play_Shot_you = int(Home_Play_Shot_you)

                    # 유효 슈팅
                    Home_Play_Shot_Target_me = Chart_html.split('legend left value')[3]
                    Home_Play_Shot_Target_me = Home_Play_Shot_Target_me.split('>')[1]
                    Home_Play_Shot_Target_me = Home_Play_Shot_Target_me.split('<')[0]

                    Home_Play_Shot_Target_you = Chart_html.split('legend right value')[3]
                    Home_Play_Shot_Target_you = Home_Play_Shot_Target_you.split('>')[1]
                    Home_Play_Shot_Target_you = Home_Play_Shot_Target_you.split('<')[0]

                    Home_Play_Shot_Target_me = int(Home_Play_Shot_Target_me)
                    Home_Play_Shot_Target_you = int(Home_Play_Shot_Target_you)

                    # 파울
                    Home_Foul_me = Chart_html.split('legend left value')[4]
                    Home_Foul_me = Home_Foul_me.split('>')[1]
                    Home_Foul_me = Home_Foul_me.split('<')[0]

                    Home_Foul_you = Chart_html.split('legend right value')[4]
                    Home_Foul_you = Home_Foul_you.split('>')[1]
                    Home_Foul_you = Home_Foul_you.split('<')[0]

                    Home_Foul_me = int(Home_Foul_me)
                    Home_Foul_you = int(Home_Foul_you)

                    # 오프사이드
                    Home_Offside_me = Chart_html.split('legend left value')[5]
                    Home_Offside_me = Home_Offside_me.split('>')[1]
                    Home_Offside_me = Home_Offside_me.split('<')[0]

                    Home_Offside_you = Chart_html.split('legend right value')[5]
                    Home_Offside_you = Home_Offside_you.split('>')[1]
                    Home_Offside_you = Home_Offside_you.split('<')[0]

                    Home_Offside_me = int(Home_Offside_me)
                    Home_Offside_you = int(Home_Offside_you)

                    # 점유율
                    Share = Chart_html.split('page_chart_1_chart_statsplus_1_chart_possession_1-wrapper')[1]
                    Share_Home = Share.split('name')[1]
                    Share_Home = Share_Home.split(':')[2]
                    Share_Home = Share_Home.split('}')[0]

                    Share_Away = Share.split('name')[2]
                    Share_Away = Share_Away.split(':')[2]
                    Share_Away = Share_Away.split(',')[0]

                    Share_Home = int(Share_Home)
                    Share_Away = int(Share_Away)

                    if home == 1:
                        sql = "INSERT INTO Soccer (Team, Result, Not_Epl, day, Enemy_name, Home_Play_1,Home_Play_2," \
                              "Home_Play_Score,Enemy_1,Enemy_2,Enemy_Score,Home_Play_Corner_me, Home_Play_Shot_me," \
                              " Home_Play_Shot_Target_me,Home_Foul_me, Home_Play_Share,Away_Play_Share,Away_Play_Corner_me, Away_Play_Shot_me," \
                              "Away_Play_Shot_Target_me, Away_Foul_me,Home_Offside_me,Away_Offside_me) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        curs.execute(sql, (
                        str(Team), int(result), int(not_epl), str(day), str(emeny_name), int(Home_play_1), int(Home_play_2),
                        int(Home_play_Score),
                        int(Ememy_1), int(Ememy_2), int(Ememy_Score), int(Home_Play_Corner_me), int(Home_Play_Shot_me),
                        int(Home_Play_Shot_Target_me),
                        int(Home_Foul_me), int(Share_Home), int(Share_Away), int(Home_Play_Corner_you),
                        int(Home_Play_Shot_you), int(Home_Play_Shot_Target_you)
                        , int(Home_Foul_you), int(Home_Offside_me), int(Home_Offside_you)))
                    else:
                        sql = "INSERT INTO Soccer (Team, Result, Not_Epl, day, Enemy_name, Home_Play_1,Home_Play_2," \
                              "Home_Play_Score,Enemy_1,Enemy_2,Enemy_Score,Home_Play_Corner_me, Home_Play_Shot_me," \
                              " Home_Play_Shot_Target_me,Home_Foul_me, Home_Play_Share,Away_Play_Share,Away_Play_Corner_me, Away_Play_Shot_me," \
                              "Away_Play_Shot_Target_me, Away_Foul_me,Home_Offside_me,Away_Offside_me) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        curs.execute(sql, (
                            str(Team), int(result), int(not_epl), str(day), str(emeny_name),
                            int(Ememy_1), int(Ememy_2), int(Ememy_Score),
                            int(Home_play_1), int(Home_play_2), int(Home_play_Score), int(Home_Play_Corner_you),
                            int(Home_Play_Shot_you), int(Home_Play_Shot_Target_you),
                            int(Home_Foul_you), int(Share_Away), int(Share_Home), int(Home_Play_Corner_me),
                            int(Home_Play_Shot_me), int(Home_Play_Shot_Target_me)
                            , int(Home_Foul_me), int(Home_Offside_you), int(Home_Offside_me)))

                        conn.commit()

                except:
                    print(url)

        driver.find_element_by_id('page_team_1_block_team_matches_3_previous').click()
        time.sleep(10)
    driver.quit()
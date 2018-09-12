import re
import csv
from datetime import date
import pymysql
# 엑셀관련
ff = open('C:/Users/Slayer/Desktop/축구분석/1차 선처리(5경기 데이터).csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)

# 엑셀 첫줄 이름 설정
csvout = csv.DictWriter(ff,['Team', 'Home', 'Result', 'Not_Epl', 'Enemy_Name', 'Home_Play_1', 'Home_Play_2', 'Home_Play_Score', 'Enemy_1', 'Enemy_2',
                            'Enemy_Score', 'Me_Play_Corner', 'Me_Play_Shot', 'Me_Play_Shot_Target', 'Me_Play_Foul', 'Me_Play_Offside', 'You_Play_Corner', 'You_Play_Shot', 'You_Play_Shot_Target', 'You_Play_Foul',
                            'You_Play_Offside', 'Home_Play_Share', 'Away_Play_Share', 'Five_Home_Play_1', 'Five_Home_Play_2', 'Five_Home_Play_Score', 'Five_Enemy_1', 'Five_Enemy_2', 'Five_Enemy_Score', 'Five_Me_Play_Corner',
                            'Five_Me_Play_Shot', 'Five_Me_Play_Shot_Target', 'Five_Me_Play_Foul', 'Five_Me_Play_Offside', 'Five_You_Play_Corner', 'Five_You_Play_Shot', 'Five_You_Play_Shot_Target', 'Five_You_Play_Foul', 'Five_You_Play_Offside', 'Five_Home_Play_Share', 'Five_Away_Play_Share','rest_time'])
csvout.writeheader()

# 변수 선언
# stack_five = 5번 루프용, stack_start = 5번 루프용, stack_time = 2번 루프용
list_out = []
a = []
stack = 0
stack_start = 0
stack_five = 0
stack_time = 0
before_time = ""

# MySql 연결
conn = pymysql.connect(host='localhost', user='root', password='autoset', db='test', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# 모르겠음
user_agent = "'Mozilla/5.0"
headers = {"User-Agent": user_agent}

# 테스트

# 휴식일수 구하는 함수 text = 현재경기, text2 = 이전경기
def time_cut(text,text2):
    text = str(text)
    year = text[:4]
    month = text[4:6]
    day = text[6:]

    text2 = str(text2)
    year2 = text2[:4]
    month2 = text2[4:6]
    day2 = text2[6:]

    year = int(year)
    month = int(month)
    day = int(day)

    year2 = int(year2)
    month2 = int(month2)
    day2 = int(day2)

    a = date(year, month, day)
    b = date(year2, month2, day2)

    result = a - b
    result = result.days
    return result

j=0

sql = "select * from soccer"
curs.execute(sql)
for row in curs:
    i = 0
    a = []
    list_out = []
    while i < 24:
        a.append(row[i])
        i = i + 1

    if stack_time >1:
        nowtime = a[23]
        a_41 = time_cut(nowtime,before_time)
        before_time = nowtime
    else:
        before_time = a[23]

    if stack_five == 0 :
        Five_Home_Play_1_a = a[5]
        Five_Home_Play_2_a = a[6]
        Five_Home_Play_Score_a = a[7]
        Five_Enemy_1_a = a[8]
        Five_Enemy_2_a = a[9]
        Five_Enemy_Score_a = a[10]
        Five_Me_Play_Corner_a = a[11]
        Five_Me_Play_Shot_a = a[12]
        Five_Me_Play_Shot_Target_a = a[13]
        Five_Me_Play_Foul_a = a[14]
        Five_Me_Play_Offside_a = a[15]
        Five_You_Play_Corner_a = a[16]
        Five_You_Play_Shot_a = a[17]
        Five_You_Play_Shot_Target_a = a[18]
        Five_You_Play_Foul_a = a[19]
        Five_You_Play_Offside_a = a[20]
        Five_Home_Play_Share_a = a[21]
        Five_Away_Play_Share_a = a[22]
    elif stack_five == 1:
        Five_Home_Play_1_b = a[5]
        Five_Home_Play_2_b = a[6]
        Five_Home_Play_Score_b = a[7]
        Five_Enemy_1_b = a[8]
        Five_Enemy_2_b = a[9]
        Five_Enemy_Score_b = a[10]
        Five_Me_Play_Corner_b = a[11]
        Five_Me_Play_Shot_b = a[12]
        Five_Me_Play_Shot_Target_b = a[13]
        Five_Me_Play_Foul_b = a[14]
        Five_Me_Play_Offside_b = a[15]
        Five_You_Play_Corner_b = a[16]
        Five_You_Play_Shot_b = a[17]
        Five_You_Play_Shot_Target_b = a[18]
        Five_You_Play_Foul_b = a[19]
        Five_You_Play_Offside_b = a[20]
        Five_Home_Play_Share_b = a[21]
        Five_Away_Play_Share_b = a[22]
    elif stack_five == 2:
        Five_Home_Play_1_c = a[5]
        Five_Home_Play_2_c = a[6]
        Five_Home_Play_Score_c = a[7]
        Five_Enemy_1_c = a[8]
        Five_Enemy_2_c = a[9]
        Five_Enemy_Score_c = a[10]
        Five_Me_Play_Corner_c = a[11]
        Five_Me_Play_Shot_c = a[12]
        Five_Me_Play_Shot_Target_c = a[13]
        Five_Me_Play_Foul_c = a[14]
        Five_Me_Play_Offside_c = a[15]
        Five_You_Play_Corner_c = a[16]
        Five_You_Play_Shot_c = a[17]
        Five_You_Play_Shot_Target_c = a[18]
        Five_You_Play_Foul_c = a[19]
        Five_You_Play_Offside_c = a[20]
        Five_Home_Play_Share_c = a[21]
        Five_Away_Play_Share_c = a[22]
    elif stack_five == 3:
        Five_Home_Play_1_d = a[5]
        Five_Home_Play_2_d = a[6]
        Five_Home_Play_Score_d = a[7]
        Five_Enemy_1_d = a[8]
        Five_Enemy_2_d = a[9]
        Five_Enemy_Score_d = a[10]
        Five_Me_Play_Corner_d = a[11]
        Five_Me_Play_Shot_d = a[12]
        Five_Me_Play_Shot_Target_d = a[13]
        Five_Me_Play_Foul_d = a[14]
        Five_Me_Play_Offside_d = a[15]
        Five_You_Play_Corner_d = a[16]
        Five_You_Play_Shot_d = a[17]
        Five_You_Play_Shot_Target_d = a[18]
        Five_You_Play_Foul_d = a[19]
        Five_You_Play_Offside_d = a[20]
        Five_Home_Play_Share_d = a[21]
        Five_Away_Play_Share_d = a[22]
    else:
        Five_Home_Play_1_e = a[5]
        Five_Home_Play_2_e = a[6]
        Five_Home_Play_Score_e = a[7]
        Five_Enemy_1_e = a[8]
        Five_Enemy_2_e = a[9]
        Five_Enemy_Score_e = a[10]
        Five_Me_Play_Corner_e = a[11]
        Five_Me_Play_Shot_e = a[12]
        Five_Me_Play_Shot_Target_e = a[13]
        Five_Me_Play_Foul_e = a[14]
        Five_Me_Play_Offside_e = a[15]
        Five_You_Play_Corner_e = a[16]
        Five_You_Play_Shot_e = a[17]
        Five_You_Play_Shot_Target_e = a[18]
        Five_You_Play_Foul_e = a[19]
        Five_You_Play_Offside_e = a[20]
        Five_Home_Play_Share_e = a[21]
        Five_Away_Play_Share_e = a[22]

    stack_five = stack_five + 1
    stack_start = stack_start + 1
    stack_time = stack_time + 1

    if stack_start > 4:
        a_23 = (Five_Home_Play_1_a + Five_Home_Play_1_b + Five_Home_Play_1_c + Five_Home_Play_1_d + Five_Home_Play_1_e) / 5
        a_24 = (Five_Home_Play_2_a + Five_Home_Play_2_b + Five_Home_Play_2_c + Five_Home_Play_2_d + Five_Home_Play_2_e) / 5
        a_25 = (Five_Home_Play_Score_a + Five_Home_Play_Score_b + Five_Home_Play_Score_c + Five_Home_Play_Score_d + Five_Home_Play_Score_e) / 5
        a_26 = (Five_Enemy_1_a + Five_Enemy_1_b + Five_Enemy_1_c + Five_Enemy_1_d + Five_Enemy_1_e) / 5
        a_27 = (Five_Enemy_2_a + Five_Enemy_2_b + Five_Enemy_2_c + Five_Enemy_2_d + Five_Enemy_2_e) / 5
        a_28 = (Five_Enemy_Score_a + Five_Enemy_Score_b + Five_Enemy_Score_c + Five_Enemy_Score_d + Five_Enemy_Score_e) / 5
        a_29 = (Five_Me_Play_Corner_a + Five_Me_Play_Corner_b + Five_Me_Play_Corner_c + Five_Me_Play_Corner_d + Five_Me_Play_Corner_e) / 5
        a_30 = (Five_Me_Play_Shot_a + Five_Me_Play_Shot_b + Five_Me_Play_Shot_c + Five_Me_Play_Shot_d + Five_Me_Play_Shot_e) / 5
        a_31 = (Five_Me_Play_Shot_Target_a+Five_Me_Play_Shot_Target_b+Five_Me_Play_Shot_Target_c+Five_Me_Play_Shot_Target_d+Five_Me_Play_Shot_Target_e)/5
        a_32 = (Five_Me_Play_Foul_a+Five_Me_Play_Foul_b+Five_Me_Play_Foul_c+Five_Me_Play_Foul_d+Five_Me_Play_Foul_e)/5
        a_33 = (Five_Me_Play_Offside_a+Five_Me_Play_Offside_b+Five_Me_Play_Offside_c+Five_Me_Play_Offside_d+Five_Me_Play_Offside_e)/5
        a_34 = (Five_You_Play_Corner_a+Five_You_Play_Corner_b+Five_You_Play_Corner_c+Five_You_Play_Corner_d+Five_You_Play_Corner_e)/5
        a_35 = (Five_You_Play_Shot_a+Five_You_Play_Shot_b+Five_You_Play_Shot_c+Five_You_Play_Shot_d+Five_You_Play_Shot_e)/5
        a_36 = (Five_You_Play_Shot_Target_a+Five_You_Play_Shot_Target_b+Five_You_Play_Shot_Target_c+Five_You_Play_Shot_Target_d+Five_You_Play_Shot_Target_e)/5
        a_37 = (Five_You_Play_Foul_a+Five_You_Play_Foul_b+Five_You_Play_Foul_c+Five_You_Play_Foul_d+Five_You_Play_Foul_e)/5
        a_38 = (Five_You_Play_Offside_a+Five_You_Play_Offside_b+Five_You_Play_Offside_c+Five_You_Play_Offside_d+Five_You_Play_Offside_e)/5
        a_39 = (Five_Home_Play_Share_a+Five_Home_Play_Share_b+Five_Home_Play_Share_c+Five_Home_Play_Share_d+Five_Home_Play_Share_e)/5
        a_40 = (Five_Away_Play_Share_a+Five_Away_Play_Share_b+Five_Away_Play_Share_c+Five_Away_Play_Share_d+Five_Away_Play_Share_e)/5

        a_23 = round(a_23, 3)
        a_24 = round(a_24, 3)
        a_25 = round(a_25, 3)
        a_26 = round(a_26, 3)
        a_27 = round(a_27, 3)
        a_28 = round(a_28, 3)
        a_29 = round(a_29, 3)
        a_30 = round(a_30, 3)
        a_31 = round(a_31, 3)
        a_32 = round(a_32, 3)
        a_33 = round(a_33, 3)
        a_34 = round(a_34, 3)
        a_35 = round(a_35, 3)
        a_36 = round(a_36, 3)
        a_37 = round(a_37, 3)
        a_38 = round(a_38, 3)
        a_39 = round(a_39, 3)
        a_40 = round(a_40, 3)

        list_out.append(
            {'Team': a[0], 'Home': a[1], 'Result': a[2], 'Not_Epl': a[3], 'Enemy_Name': a[4], 'Home_Play_1': a[5],
             'Home_Play_2': a[6], 'Home_Play_Score': a[7], 'Enemy_1': a[8], 'Enemy_2': a[9], 'Enemy_Score': a[10],
             'Me_Play_Corner': a[11], 'Me_Play_Shot': a[12], 'Me_Play_Shot_Target': a[13], 'Me_Play_Foul': a[14],
             'Me_Play_Offside': a[15], 'You_Play_Corner': a[16], 'You_Play_Shot': a[17], 'You_Play_Shot_Target': a[18],
             'You_Play_Foul': a[19], 'You_Play_Offside': a[20],
             'Home_Play_Share': a[21], 'Away_Play_Share': a[22], 'Five_Home_Play_1': a_23, 'Five_Home_Play_2': a_24,
             'Five_Home_Play_Score': a_25, 'Five_Enemy_1': a_26, 'Five_Enemy_2': a_27, 'Five_Enemy_Score': a_28,
             'Five_Me_Play_Corner': a_29, 'Five_Me_Play_Shot': a_30,
             'Five_Me_Play_Shot_Target': a_31, 'Five_Me_Play_Foul': a_32, 'Five_Me_Play_Offside': a_33,
             'Five_You_Play_Corner': a_34, 'Five_You_Play_Shot': a_35, 'Five_You_Play_Shot_Target': a_36,
             'Five_You_Play_Foul': a_37, 'Five_You_Play_Offside': a_38, 'Five_Home_Play_Share': a_39,
             'Five_Away_Play_Share': a_40, 'rest_time': a_41})
        csvout.writerows(list_out)
        j = j + 1

    if stack_five == 5 :
            stack_five = 0



    if stack>5:
        stack= stack + 1
print(j)
ff.close()
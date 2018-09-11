import re
import csv
from datetime import date

# 엑셀관련
ff = open('C:/Users/Slayer/Desktop/공유할것 (1)/collectl_output_EP_D_64.csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)

# 엑셀 첫줄 이름 설정
csvout = csv.DictWriter(ff,['Team', 'Home', 'Away', 'Result', 'Not_Epl', 'Enemy_Name', 'Home_play0', 'Home_Play_1', 'Home_Play_2', 'Home_Play_Score', 'Enemy_1', 'Enemy_2', 'Enemy_Score', 'Me_Play_Corner', 'Me_Play_Shot', 'Me_Play_Offside', 'You_Play_Corner', 'You_Play_Shot', 'You_Play_Offside', 'Home_Play_Share', 'Away_Play_Share', 'Five_Home_play0', 'Five_Home_Play_1', 'Five_Home_Play_2', 'Five_Home_Play_Score', 'Five_Enemy_1', 'Five_Enemy_2', 'Five_Enemy_Score', 'Five_Me_Play_Corner', 'Five_Me_Play_Shot', 'Five_Me_Play_Offside', 'Five_You_Play_Corner', 'Five_You_Play_Shot', 'Five_You_Play_Offside', 'Five_Home_Play_Share', 'Five_Away_Play_Share','rest_time'])
csvout.writeheader()

# 변수 선언
list_out = []
a = []
stack = 0

# 테스트
a = 20180505
b = 20180512
c = 20170228
"""
list_out.append({'Team':a[0], 'Home':a[1], 'Result':a[2], 'Lose':a[3], 'Not_Epl':a[4], 'Enemy_Name':a[5], 'Home_play0':a[6], 'Home_Play_1':a[7], 'Home_Play_2':a[8], 'Home_Play_Score':a[9], 'Enemy_1':a[10], 'Enemy_2':a[11], 'Enemy_Score':a[12], 'Me_Play_Corner':a[13], 'Me_Play_Shot':a[14], 'Me_Play_Offside':a[15], 'You_Play_Corner':a[16], 'You_Play_Shot':a[17], 'You_Play_Offside':a[18], 'Home_Play_Share':a[19], 'Away_Play_Share':a[20], 'Five_Home_play0':a[21], 'Five_Home_Play_1':a[22], 'Five_Home_Play_2':a[23], 'Five_Home_Play_Score':a[24], 'Five_Enemy_1':a[25], 'Five_Enemy_2':a[26], 'Five_Enemy_Score':a[27], 'Five_Me_Play_Corner':a[28], 'Five_Me_Play_Shot':a[29], 'Five_Me_Play_Offside':a[30], 'Five_You_Play_Corner':a[31], 'Five_You_Play_Shot':a[32], 'Five_You_Play_Offside':a[33], 'Five_Home_Play_Share':a[34], 'Five_Away_Play_Share':a[35], 'rest_time':a[36]})
csvout.writerows(list_out)
"""

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
    return result

tol = time_cut(a,c)

print(tol.days)

ff.close()

if stack>5:
    stack= stack + 1
else:
    pass


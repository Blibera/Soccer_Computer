import pymysql


a = 100
b = 200
c = 300
d = 400
e = 500
f = 600
g = 700

# stack_five = 5번 루프용, stack_start = 5번 넘게 루프하면 시작하게 하는 변수
stack_five = 0
stack_start = 0
h = []
i = 0
# MySql 연결
conn = pymysql.connect(host='localhost', user='root', password='autoset', db='test', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# 모르겠음
user_agent = "'Mozilla/5.0"
headers = {"User-Agent": user_agent}

sql = "select * from soccer"
curs.execute(sql)

i = 0
for row in curs:
    i = i + 1
print(i)
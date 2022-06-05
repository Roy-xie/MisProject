import requests
import pymysql
from matplotlib.style import context

conn = pymysql.connect(host='127.0.0.1' , port=3306, passwd='123', user = 'test',
db='mis', )
cursor=conn.cursor()
print(conn)
sql ="SELECT * FROM `year110` WHERE `學校名稱` = '國立中興大學'"
cursor.execute(sql)
rows = cursor.fetchall()
context = {}
# context["searchschool"] = rows
for i in rows:
    context["searchschool"] =i
print(rows)
print(context["searchschool"])
cursor.close()
conn.close()

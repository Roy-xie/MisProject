import requests
import pymysql
from matplotlib.style import context

conn = pymysql.connect(host='127.0.0.1' , port=3306, passwd='123', user = 'test',
db='mis', )
cursor=conn.cursor(dictionary=True)
print(conn)
sql ="SELECT * FROM `year110` WHERE `school_name` = '國立中興大學'"
cursor.execute(sql)
rows = cursor.fetchone()
context = {}
# context["searchschool"] = rows
# rows = mysqli_fetch_array(rows)

cursor.close()
conn.close()

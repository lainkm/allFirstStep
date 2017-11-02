import pymysql
import pandas as pd 

con = pymysql.connect(host = "localhost", user = 'root', db = 'students', passwd = '666666')
sql = "SELECT * FROM lesson"
df = pd.read_sql(sql, con)
print(df)

cursor = con.cursor()
# cursor.execute("insert into lesson(lesson_id) values(550)")
for i in range(20, 30, 2):
	cursor.execute("insert into lesson(lesson_id) values(55)")
con.commit()
df = pd.read_sql(sql, con)
print(df)
cursor.close()
con.close()

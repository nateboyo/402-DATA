import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Password')
cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS menagerie')
table = cursor.fetchall()
conn.commit()
cursor.close()
conn.close()
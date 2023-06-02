import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Password')
cursor = conn.cursor()
cursor.close()
conn.close()
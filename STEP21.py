import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Password', database='menagerie')
cursor = conn.cursor()
select_query = "SELECT name, birth FROM pet;"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    name, birth = row
    print(f"Name: {name}, Birth: {birth}")
cursor.close()
conn.close()
import sqlite3

connection =sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
create table STUDENT(NAME VARCHAR(25),class VARCHAR(25),SECTION VARCHAR(25),marks int);
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('sandesh','A','Ai',90)''')
cursor.execute('''Insert Into STUDENT values('san','B','cs',70)''')
cursor.execute('''Insert Into STUDENT values('abc','C','AiML',20)''')
cursor.execute('''Insert Into STUDENT values('sil','D','devops',80)''')


print("records are ")

data=cursor.execute('''select * from student''')

for row in data:
    print(row)


connection.commit()
connection.close()
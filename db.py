import sqlite3
import os

PATH = os.path.abspath(__file__ + '/..')

con = sqlite3.connect(os.path.join(PATH, "mydb.db"))

cursor = con.cursor()

# sql1 = '''
# CREATE TABLE students (
#     name varchar(255),
#     surname varchar(255),
#     age int,
#     password varchar(255)
# );
# '''
# add_student_sql = '''
# INSERT INTO students
# VALUES ('Angrew', 'Drugha', '16', '9876');
# ''' 
select_student_sql = '''
SELECT * FROM students;
'''
result = cursor.execute(select_student_sql)

print(result.fetchall())
con.commit()
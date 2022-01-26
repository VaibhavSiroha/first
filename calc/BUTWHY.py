import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234')
conn.autocommit=True
if conn.is_connected():
    print('connected succesfully')
else:
    print('not connected')
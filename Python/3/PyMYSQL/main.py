import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost ',
    user = 'root',
    password ='',
    port = '3306 ',
    database ='prueba_1 '
)

mycursor = mydb.cursor()

mycursor.execute('SELECT  * FROM employee')
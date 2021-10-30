import pymysql as MySQLdb
import random

def generateSQL():
    nombres = ["Juan","Pedro","Ana","Maria","Merced","John","Ivan","Melchor","James","Monica"]
    apellidos = ["Perez","Garcia","Mondragon","Torres","Gonzalez","Ramirez","Doe"]
    sql = ""
    for ID in range(1,101):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        sql += "INSERT INTO `informacion_personal` (`matricula`, `Nombre`, `Apellido`, `Fecha_Nacimiento`)"
        sql += " VALUES ('"+str(ID)+"', '"+nombre+"', '"+apellido+"', '2021-10-07');\n"
    return sql

def insertData():
    miConexion = MySQLdb.connect( host='localhost', user= 'root', passwd='', db='test2')
    cur = miConexion.cursor()
    nombres = ["Juan","Pedro","Ana","Maria","Merced","John","Ivan","Melchor","James","Monica"]
    apellidos = ["Perez","Garcia","Mondragon","Torres","Gonzalez","Ramirez","Doe"]
    sql = "INSERT INTO `informacion_personal` (`matricula`, `Nombre`, `Apellido`, `Fecha_Nacimiento`)"
    sql += " VALUES (%s, %s, %s, %s)"
    val = []
    for ID in range(1,101):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        row = (str(ID), nombre, apellido, '2021-10-07')
        val.append(row)
    print(val)
    #cur.execute(sql)
    cur.executemany(sql,val)
    miConexion.commit()
    miConexion.close()

#Ejemplo 1: como generar SQL (para copiar y pegar)
# print(generateSQL())

#Ejemplo 2: como insertar data
insertData()

# miConexion = MySQLdb.connect( host='localhost', user= 'root', passwd='', db='test2')
# miConexion = MySQLdb.connect( host='localhost', user= 'root', passwd='')
# cur = miConexion.cursor()
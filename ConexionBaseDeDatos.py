#cpnexion con base de datos sqlite3
import sqlite3 as dbapi
from sqlite3 import DatabaseError, OperationalError

#nivel de la api
print(dbapi.apilevel)

#nos indica que nivel de seguridad tiene usar hilos con sqlite
print(dbapi.threadsafety)

#estilo de parámetros, en este caso usaremos consultas con ?
print(dbapi.paramstyle)

#establecemos la conexion, entre parámetros ponemos la dirección de la base de datos, si no existe la crea
bbdd = dbapi.connect("bbdd.dat")

#creó un objeto de tipo sqlite connect, la base se crea en local
print(bbdd)

#creamos el objeto cursos
cursor = bbdd.cursor()
print(cursor)

#Ejecutamos una consulta y capturamos la excepción si la tabla ya existe
'''
try:
    cursor.execute("""Create table usuarios (dni text, nome text, edade int)""")
except OperationalError as e:
    print("Error al crear la tabla: " + str(e))
    bbdd.close()
'''

#vamos a hacer insercciones
'''
try:
    cursor.execute("""insert into usuarios values('123456789K','Ana Ruiz',27)""")
    cursor.execute("""insert into usuarios values('123123123F','Pablo Capelo',89)""")
    cursor.execute("""insert into usuarios values('69696969J','Jorge de los bustos',45)""")
    cursor.execute("""insert into usuarios values('111223345','Pablo motos',49)""")
    bbdd.commit() #SÚPER IMPORTANTE PONER ESTO PARA CONFIRMAR LOS CAMBIOS
except DatabaseError as e:
    print("Error al insertar datos en la tabla: " + str(e))
    bbdd.close()
'''

#! / usr / bin / python
# - * - coding: UTF-8 - * -
import os, sys
import signal, os, sys
import MySQLdb #conexion a MySQL
import pymssql #Conexion a SQL Server
conexion_mysql = MySQLdb.connect(host = '10.248.204.43', user = 'root', passwd = 'sahc', db = 'Biblioteca')
server = "EXP-AXPOS10"
user = "esolis"
password = "Python@Monitor"
base = "StoragePython"
conexion_sql = pymssql.connect(server, user, password, base)

cur = conexion_mysql.cursor()
cur2 = conexion_sql.cursor()
consulta = ('SELECT *, IF(time >= 10,"Bad","Good") AS Estado FROM INFORMATION_SCHEMA.PROCESSLIST WHERE id <> connection_id()')
cur.execute(consulta)
for row in cur.fetchall():
    resultado = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
    sql = "INSERT INTO LogKillProcesstMySQL VALUES (" + str(row[0]) + "," + "'" + (row[1] or '') + "'" + "," + "'" + (row[2] or '') + "'" + "," + "'" + (row[3] or '') + "'" + "," + "'" + (row[4] or '') + "'" + "," + str(row[5]) + "," + "'" + (row[6] or '') + "'" + "," + "'" + (row[7] or '') + "'" + "," + "GETDATE()" + ")"
    cur2.execute(sql)
    conexion_sql.commit()
    print "Datos Guardados Exitosamente"
    if row[0] == row[0]:
        matar = "KILL " + str(row[0])
        cur.execute(matar)
        #conexion_mysql.commit()
        print "Proceso Eliminado"
conexion_mysql.commit()
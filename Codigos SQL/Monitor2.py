# -*- encoding: utf-8 -*-
#Libreias
#import pymssql
from time import sleep
import os,sys
from pprint import pprint

import pymssql

reload(sys)
sys.setdefaultencoding('utf8')

server = "EXP-AXPOS10"
user = "esolis"
password = "Python@Monitor"
base = "StoragePython"

Conection = "select se.servidor, se.[user], se.Pass from servers se left join scripts sc on ses.idq = sc.idq order by se.servidor, ses.idq "
validacion = "XPSATURNO"

def ejecutaSp(server, user, password, base):
    try:
        #llenado = "SELECT SUBSTRING(" + row2[2] + "," + "20, 40) FROM Logdat"
        hora = 'DECLARE @timeFrom time(4) = GETDATE() ' \
               'DECLARE @timeTo time(3) = @timeFrom ' \
               'SELECT @timeTo AS "time(3)", @timeFrom AS "time(4)"'
        query = "EXEC sys.xp_readerrorlog 6, 1, N'login', N'failed'"
        select = "SELECT @@servername"

        con3 = pymssql.connect(server, user, password, base)
        cursor3 = con3.cursor()
        cursor3.execute(hora)
        for row3 in cursor3.fetchall():
            resultado3 = row3[0], row3[1]

        con = pymssql.connect(server, user, password, base)
        cursor = con.cursor()
        cursor.execute(select)

        for row in cursor.fetchall():
            resultado = row[0]

            con2 = pymssql.connect(server, user, password, base)
            cursor2 = con2.cursor()
            cursor2.execute(query)
        for row2 in cursor2.fetchall():
            resultado = row2[0], row2[1], row2[2]
            #print resultado
            #exit(0)
            insert = "INSERT INTO LogData(fechahora,descripcion,servidor,horaCaptura,fechaCaptura) VALUES(" + "'" + str(row2[0]) + "'" + "," + "'" + (row2[2].replace('\'','\'\'') or '') + "'"+ "," + "'" + row[0] + "'" + "," + "'" + str(row3[1]) + "'" + "," + "GETDATE()" + ")"
            #insert2 = "INSERT INTO LogData(futuriusuario) VALUES (SELECT SUBSTRING(descripcion,20, 40) FROM LogData)"
            #print insert
            #print insert2
            #exit(0)
            try:
                cursor2.execute(insert)
                #cursor2.execute(insert2)
                con2.commit()
                print "Datos Insertados"
            except Exception as error:
                print('Ocurrió un problema al insertar: ' + str(error))
                exit(0)
    except Exception as error:
        print('Ocurrió un problema en la conexión con el servidor principal: ' + server + ' e usuario: ' + user + ' - ' + str(error))

try:
    ejecutaSp(server, user, password, base)
    exit(0)
except Exception as error:
    print('Ocurrió un problema en la conexión con la funcion en el servidor principal: ' + server + ' e usuario: ' + user + ' - ' + str(error))
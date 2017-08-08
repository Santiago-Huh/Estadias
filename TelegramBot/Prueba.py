import pymssql
server = "10.248.1.209"
user = "esolis"
password = "Python@Monitor"
base = "StoragePython"
conexion_sql = pymssql.connect(server, user, password, base)

cur = conexion_sql.cursor()
consulta = "select ID, Usuario, DiaGuardado from LogKillProcesstMySQL"
cur.execute(consulta)
for row in cur.fetchall():
	resultado = row[0], row[1], row[2]
	print resultado

from pymongo import MongoClient
con = MongoClient()
db = con.BD

alumno = { "Nombre" : "Gaby", "Matricula" : "1502265", "Edad" : "20", "Genero" : "Femenino", "Carrera" : "N/A"}
alumnos = db.tabla
alumnos.insert(alumno)

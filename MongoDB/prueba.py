from pymongo import MongoClient
con = MongoClient()

db = con.test

user = {
	'nombre' : 'Saul',
	'edad' : 38,
	'localidad' : 'Monterrey',
	'curp' : 'NDUBD88DND87'
}

use = db.users
use.insert_one(user)

print 'Insertado Correctamente' + str(use.inserted_id)

for row in use.find():
	print row

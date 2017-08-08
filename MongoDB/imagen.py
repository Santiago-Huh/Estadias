#!/usr/bin/env python
import Image
import pymongo
import base64

from PIL import Image, ImageOps
from pymongo import MongoClient
con = MongoClient()
db = con.test

image = 'masexito.jpg'

img = Image.open(image)
#img.save('/home/santiago/Documents/Python/img/exito2.jpg')
#encoded = base64.b64encode(img)
with open(image, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

user = {
	'nombre' : 'Saul',
	'edad' : 38,
	'localidad' : 'Monterrey',
	'curp' : 'NDUBD88DND87',
	'imagen' : encoded_string
}

use = db.users
use.insert_one(user)

print 'Insertado Correctamente' + str(use.inserted_id)

for row in use.find():
	print row

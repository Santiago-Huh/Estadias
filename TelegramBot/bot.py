# -*- encoding: UTF8-*- #
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pymssql
import MySQLdb

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
	update.message.reply_text('Bienvenido a BotSQL, ¿En que te puedo ayudar? '\
						'Para ver mis comandos usa:  /help')
def help(bot, update):
	update.message.reply_text('Estos son mis comandos:\n'\
					'Tablas Cargo: /cargo\n'\
					'Tablas Almacenes: /almacenes\n'\
					'Tablas Autor: /autores\n'\
					'Tablas Clientes: /clientes\n'\
					'Tablas Detalles nota: /detalles\n')
def cargo(bot, update):
	conexion_mysql = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'sahc',db = 'Biblioteca')
	cur = conexion_mysql.cursor()
	consulta = "SELECT * FROM Cargo"
	cur.execute(consulta)
	for row in cur.fetchall():
		resultado = row[0], row[1]
		update.message.reply_text(resultado)
	print "Se imprimio resultados Cargo"

def almacen(bot, update):
	conexion_mysql = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'sahc',db = 'Biblioteca')
	cur2 = conexion_mysql.cursor()
	consulta2 = "SELECT * FROM Almacenes"
	cur2.execute(consulta2)
	for row2 in cur2.fetchall():
		resultado2 = row2[0], row2[1], row2[2], row2[3]
		update.message.reply_text(resultado2)
	print ("Se imprimio resultados Almacenes")

def autor(bot, update):
        conexion_mysql = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'sahc',db = 'Biblioteca')
        cur3 = conexion_mysql.cursor()
        consulta3 = "SELECT * FROM Autor"
        cur3.execute(consulta3)
        for row3 in cur3.fetchall():
                resultado3 = row3[0], row3[1], row3[2], row3[3]
                update.message.reply_text(resultado3)
        print ("Se imprimio resultados Autor")

def cliente(bot, update):
        conexion_mysql = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'sahc',db = 'Biblioteca')
        cur4 = conexion_mysql.cursor()
        consulta4 = "SELECT * FROM Clientes"
        cur4.execute(consulta4)
        for row4 in cur4.fetchall():
                resultado4 = row4[0], row4[1], row4[2]
                update.message.reply_text(resultado4)
        print ("Se imprimio resultados Clientes")

def detalle(bot, update):
        conexion_mysql = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'sahc',db = 'Biblioteca')
        cur5 = conexion_mysql.cursor()
        consulta5 = "SELECT * FROM Detalle_nota_venta"
        cur5.execute(consulta5)
        for row5 in cur5.fetchall():
                resultado5 = row5[0], row5[1], row5[2]
                update.message.reply_text(resultado5)
        print ("Se imprimio resultados de Detalles Nota Venta")

def echo(bot, update):
	update.message.reply_text(update.message.text)

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
	updater = Updater("431796863:AAE3n-2Va42qA6Jp4YxFPnNZX8dJ8ICLlUo")

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("cargo", cargo))
	dp.add_handler(CommandHandler("almacenes", almacen))
	dp.add_handler(CommandHandler("autores", autor))
	dp.add_handler(CommandHandler("clientes", cliente))
	dp.add_handler(CommandHandler("detalles", detalle))

	dp.add_handler(MessageHandler(Filters.text, echo))

	dp.add_error_handler(error)

	updater.start_polling()

	updater.idle()

if __name__=='__main__':
	main()

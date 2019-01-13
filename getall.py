
import mysql.connector
from mysql.connector import Error

def getall(name):
	try:
		cnx = mysql.connector.connect(user='sql9273861', password='eCvI714qdd',
                              	host='sql9.freesqldatabase.com',
                              	database='sql9273861')
		cursor = cnx.cursor()
		query = "SELECT * FROM `" + name + "`"
		cursor.execute(query)
		valrow = []
		for row in cursor:
			valrow.append(row)
		cursor.close()
		cnx.close()
		return valrow
	except Error as e:
		print("Error while connecting to MySQL database", e)

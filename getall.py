
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
		fullrow = []
		partrow = []
		for row in cursor:
			fullrow.append(row)
			partrow.append(row[1])
		cursor.close()
		cnx.close()
		finalrow = [fullrow, partrow]
		return finalrow
	except Error as e:
		print("Error while connecting to MySQL database", e)


import mysql.connector
from mysql.connector import Error

def keywordreturn():
	try:
		cnx = mysql.connector.connect(user='sql9273861', password='eCvI714qdd',
                              	host='sql9.freesqldatabase.com',
                              	database='sql9273861')
		cursor = cnx.cursor()
		query = "SELECT * FROM keywords"
		cursor.execute(query)
		management = []
		legal = []
		financial = []
		humanresc = []
		innovation = []
		for row in cursor:
			management.append(row[0])
			legal.append(row[1])
			financial.append(row[2])
			humanresc.append(row[3])
			innovation.append(row[4])
		cursor.close()
		cnx.close()
		allkeywords = [management, legal, financial, humanresc, innovation]
		return allkeywords
	except Error as e:
		print("Error while connecting to MySQL database", e)

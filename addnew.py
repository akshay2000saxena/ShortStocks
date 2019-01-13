import mysql.connector
from mysql.connector import Error

def addnew (name, tagID, RelevBool):
	try:	
		cnx = mysql.connector.connect(user='sql9273861', password='eCvI714qdd',
                              host='sql9.freesqldatabase.com',
                              database='sql9273861')
		cursor = cnx.cursor()
		query1 = "CREATE TABLE IF NOT EXISTS `" + name + "` (tagID INT, RelevBool INT)"
		cursor.execute(query1)
		cnx.commit()
		query2 = "INSERT INTO `" + name + "` (tagID, RelevBool) VALUES (%s, %s)"
		cursor.execute(query2, (tagID, RelevBool))
   		cnx.commit()
   		cursor.close()
		cnx.close()
	except Error as e:
		print("Error while connecting to MySQL database", e)


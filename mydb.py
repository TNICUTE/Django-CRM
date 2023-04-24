import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '1@Aethanoo'

	)

# prepare a cursor object
cursorobject = database.cursor()

# create a database
cursorobject.execute("CREATE  DATABASE nicfirstdb")

print("ALL DONE!")


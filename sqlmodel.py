import sqlite3
connection = ""


def initialise_database():
	global connection	

	print("Creating database if it does not already exist")
	connection = sqlite3.connect('prinotes.sql')

	print("Creating tables if they do not already exist")
	connection.execute("CREATE TABLE IF NOT EXISTS user(userid INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(100), passwordhash VARCHAR(1000))")

	connection.execute("CREATE TABLE IF NOT EXISTS note(noteid INTEGER PRIMARY KEY AUTOINCREMENT,	notetitle VARCHAR(100),	notecontents VARCHAR(10000), userid INTEGER, FOREIGN KEY(userid) REFERENCES user(userid))")

	connection.commit()


def close_database():
	global connection

	print("Closing database")
	connection.close()


def add_user(username, passwordhash):
	global connection

	connection.execute("SELECT userid FROM user WHERE username = ?", (username, ))
	check = connection.cursor().fetchone() 
	print(check)
#
#	if check is None:
#		print("Adding user " + username + " to the database")
#		connection.execute("INSERT INTO user (username, passwordhash) VALUES(?, ?)", (username, passwordhash))
#		return True
#	else:
#		print("Username already exists. Please choose another")		
#		return False
	
	connection.commit()
						 
def check_password(username, passwordhash):
	
	return

# Change user password
# Add note
# Edit note
# Delete note
# Get user notes

# Testing
initialise_database()

add_user("Louis", "lol")
output = connection.execute("SELECT * FROM user")
print(list(output))

close_database()

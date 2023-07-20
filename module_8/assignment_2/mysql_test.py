#Assignment 8.2
#July 18th, 2023
#Jeff Haberman
#CYBR 410
#Python script to make connection to MySQL database

#import mysql connector for db connection commands
import mysql.connector
from mysql.connector import errorcode

#create login credentials for mysql database connection
config = {
    'user': 'pysports_user',
    'password': 'MySQL8IsGreat!',
    'host': '127.0.0.1',
    'database': "pysports",
    'raise_on_warnings': True
}

#database connection attempt
try:
    #connect to the database with variable, add to variable for printing
    db = mysql.connector.connect(**config)

    #print successful connection to database
    print("\n Database user {} connected to MySQL on host {} with database {} ".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

#error handling section
except mysql.connector.Error as err:

    #error handling for invalid credentials
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print (' The supplied username or password are invalid')

    #error handling for invalid database
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print ('  The specified database does not exist')

    #error handling for all other errors
    else:
        print(err)

#close the database connection
finally:
    db.close()
    
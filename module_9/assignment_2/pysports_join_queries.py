#Assignment 8.2
#July 25th, 2023
#Jeff Haberman
#CYBR 410
#Python script to connect to MySQL database and do an inner join query

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

try:
    #connect to the database with variable, add to variable for printing
    db = mysql.connector.connect(**config)

      #player table query statement
    inner_join_query = ("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #set cursor position for query
    cursor = db.cursor()

    #perform player table query statement
    cursor.execute(inner_join_query)

    #print out all player records
    print("-- DISPLAYING PLAYER RECORDS --")
    for (player_id, first_name, last_name, team_name) in cursor:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team Name: {}".format(team_name))
        print("\n")
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

input("\nPress any key to continue...")
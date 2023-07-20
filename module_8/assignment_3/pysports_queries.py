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

    #set cursor position for query
    cursor = db.cursor()

    #team table query statement
    team_query = ("SELECT team_id, team_name, mascot FROM team")

    #player table query statement
    player_query = ("SELECT player_id, first_name, last_name,team_id FROM player")

    #perform team table query statement
    cursor.execute(team_query)

    #print successful connection to database
    print("\n Database user {} connected to MySQL on host {} with database {} ".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")
    
    #print out all team records
    print("\n\n-- DISPLAYING TEAM RECORDS --")

    for (team_id, team_name, mascot) in cursor:
        print("Team ID: {}".format(team_id))
        print("Team Name: {}".format(team_name))
        print("Mascot: {}".format(mascot))
        print("\n")
   
    #perform player table query statement
    cursor.execute(player_query)

    #print out all player records
    print("-- DISPLAYING PLAYER RECORDS --")
    for (player_id, first_name, last_name, team_id) in cursor:
        print("Player ID: {}".format(player_id))
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Team ID: {}".format(team_id))
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
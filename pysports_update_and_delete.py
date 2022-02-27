""" This assignment shows that I am showing all players, adding a player, updating that player, then deleting the added player."""


import mysql.connector
from mysql.connector import errorcode


""" Setting the configuration for the database"""
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursor, title):

    # I am doing the inner join query again 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # displaying all records after the inner join query 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # showing players in the shown format below
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:

    db = mysql.connector.connect(**config) # this part connects to the database, configuration was called before

    cursor = db.cursor()

    # adding a player to the pysports database 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # adding the player to 1 as called out 
    player_data = ("Strider", "Newago", 1)

    # executing the player and pertaining data
    cursor.execute(add_player, player_data)
 
    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")
 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Michael', last_name = 'Jackson' WHERE first_name = 'Strider'")

    cursor.execute(update_player)

    # this will show the update from Strider to Michael 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # deleting Michael Jackson from table
    delete_player = ("DELETE FROM player WHERE first_name = 'Michael'")

    cursor.execute(delete_player)
    # shows that Michael has been deleted
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()
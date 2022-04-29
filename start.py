from BDD.integration.joueur_controller import joueur_controller
from BDD.integration.game_controller import game_controller
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    finally:
        return conn

conn_db = create_connection("migration.db")
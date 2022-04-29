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

if __name__ == '__main__':
    conn_db = create_connection("migration.db")
    cursor_obj = conn_db.cursor()

    table_score = """ CREATE TABLE IF NOT EXISTS score (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            score integer NOT NULL
                        ); """

    table_joueur = """ CREATE TABLE IF NOT EXISTS joueur (
                            id integer PRIMARY KEY,
                            couleur text NOT NULL,
                            score integer NOT NULL
                        ); """

    table_game = """ CREATE TABLE IF NOT EXISTS game (
                            id integer PRIMARY KEY,
                            joueur1 text NOT NULL,
                            joueur2 text NOT NULL,
                            score1 integer NOT NULL,
                            score2 integer NOT NULL,
                            foreign key(joueur1) references joueur(id)
                                on delete cascade
                                on update cascade,
                            foreign key(joueur2) references joueur(id)
                                on delete cascade
                                on update cascade,
                            foreign key(score1) references joueur(score)
                                on delete cascade
                                on update cascade,
                            foreign key(score2) references joueur(score)
                                on delete cascade
                                on update cascade
                        ); """

    try :
        cursor_obj.execute(table_score)
        cursor_obj.execute(table_joueur)
        cursor_obj.execute(table_game)
        conn_db.commit()
        conn_db.close()
        print("Table created successfully")
    except Error as e:
        print(e)
        
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

class joueur_controller:
    def __init__(self, id, couleur, score):
        self.id = id
        self.couleur = couleur
        self.score = score

    @staticmethod
    def create_joueur(conn, couleur, score):
       
        sql = ''' INSERT INTO joueur(couleur, score)
                  VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (couleur, score))
        conn.commit()
        print("player created successfully")
    
    @staticmethod
    def get_joueur(conn, id):
        sql = ''' SELECT * FROM joueur WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        row = cur.fetchone()
        print("player id: ", row[0])
        print("player couleur: ", row[1])
        print("player score: ", row[2])
    
    @staticmethod
    def update_joueur(conn, id, couleur, score):
        sql = ''' UPDATE joueur
                  SET couleur=?, score=?
                  WHERE id=? ; '''
        cur = conn.cursor()
        cur.execute(sql, (couleur, score, id))
        conn.commit()

    @staticmethod
    def delete_joueur(conn, id):
        sql = ''' DELETE FROM joueur WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        print("player deleted successfully")

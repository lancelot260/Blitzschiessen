import sqlite3

class game_controller:

    def __init__(self, id, joueur1, joueur2, score1, score2):
        self.id = id
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score2

    @staticmethod
    def create_game(conn, joueur1, joueur2, score1, score2):
        sql = ''' INSERT INTO game(joueur1, joueur2, score1, score2)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (joueur1, joueur2, score1, score2))
        conn.commit()
        print("game created successfully")

    @staticmethod
    def get_game(conn, id):
        sql = ''' SELECT * FROM game WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        row = cur.fetchone()
        print("game id: ", row[0])
        print("game joueur1: ", row[1])
        print("game joueur2: ", row[2])
        print("game score1: ", row[3])
        print("game score2: ", row[4])

    @staticmethod
    def get_best_game(conn):
        sql = ''' SELECT * FROM game ORDER BY score1 OR score2 DESC LIMIT 5 '''
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    @staticmethod
    def update_game(conn, id, joueur1, joueur2, score1, score2):
        sql = ''' UPDATE game
                  SET joueur1=?, joueur2=?, score1=?, score2=?
                  WHERE id=? ; '''
        cur = conn.cursor()
        cur.execute(sql, (joueur1, joueur2, score1, score2, id))
        conn.commit()

    @staticmethod
    def delete_game(conn, id):
        sql = ''' DELETE FROM game WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        print("game deleted successfully")
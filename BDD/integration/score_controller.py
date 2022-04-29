import sqlite3

class score_controller:

    def __init__(self, id, joueur1, joueur2, score1, score2):
        self.id = id
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score2
    
    @staticmethod
    def create_score(conn, joueur1, joueur2, score1, score2):
        sql = ''' INSERT INTO score(joueur1, joueur2, score1, score2)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (joueur1, joueur2, score1, score2))
        conn.commit()
        print("score created successfully")

    @staticmethod
    def get_score(conn, id):
        sql = ''' SELECT * FROM score WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        row = cur.fetchone()
        print("score id: ", row[0])
        print("score joueur1: ", row[1])
        print("score joueur2: ", row[2])
        print("score score1: ", row[3])
        print("score score2: ", row[4])

    @staticmethod
    def update_score(conn, id, joueur1, joueur2, score1, score2):
        sql = ''' UPDATE score
                  SET joueur1=?, joueur2=?, score1=?, score2=?
                  WHERE id=? ; '''
        cur = conn.cursor()
        cur.execute(sql, (joueur1, joueur2, score1, score2, id))
        conn.commit()

    @staticmethod
    def delete_score(conn, id):
        sql = ''' DELETE FROM score WHERE id = ? '''
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        print("score deleted successfully")
        
import pymysql


class Database:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="password",
            database="registro",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_voti(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM voti")
            return cursor.fetchall()

    def get_voti_studente(self, nome):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM voti WHERE studente=%s",
                (nome,)
            )
            return cursor.fetchall()

    def inserisci_voto(self, studente, materia, voto):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO voti (studente,materia,voto) VALUES (%s,%s,%s)",
                (studente, materia, voto)
            )
            self.conn.commit()
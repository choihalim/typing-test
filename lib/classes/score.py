from . import CONN, CURSOR
from datetime import date

class Score:
    def __init__(self, user_id, wpm, accuracy, date=None):
        self.user_id = user_id
        self.wpm = wpm
        self.accuracy = accuracy
        self._date = date
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) is str and 0 < len(date) <= 10:
            self._date = date
        else:
            raise Exception("Date must be a string greater than 0 and less than or equal to 10 characters long.")

    def update_user_wpm(self, wpm):
        self.wpm = wpm

    def update_user_acc(self, acc):
        self.accuracy = acc

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS scores(
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                wpm INTEGER,
                accuracy FLOAT,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        print("Score table creation attempted. Please check your console")

    @classmethod
    def create(cls, user_id, wpm, accuracy, date):
        new_score = Score(user_id, wpm, accuracy, date)
        if new_score:
            sql = f"""
                INSERT INTO scores (user_id, wpm, accuracy, date)
                VALUES ({new_score.user_id}, {new_score.wpm}, {new_score.accuracy}, '{new_score.date}')
            """
            CURSOR.execute(sql)
            score_id = CURSOR.execute('SELECT last_insert_rowid() FROM scores').fetchone()[0]
            new_score = CURSOR.execute(f'SELECT * FROM scores WHERE id = {score_id}').fetchone()
            return new_score
        else:
            raise Exception('Could not create score. Check data and try again.')
        
    @classmethod
    def all(cls):
        sql = "SELECT * FROM scores"
        scores = CURSOR.execute(sql).fetchall()
        return scores


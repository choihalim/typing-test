from . import CONN, CURSOR
import re

class User:
    def __init__(self, username, id=None):
        self._username = username
        self.id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name):
        if type(name) == str and 5 < len(name) < 15 and re.search(r'[A-Z]', name):
            # re (regular expression) allows you to specify patterns
            self._username = name
        else:
            raise Exception("Username must be a string with more than 5 characters, less than 15 characters, and include at least one uppercase letter.")

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT
            )
        """)
        print("Table creation attempted. Please check your console")

    @classmethod
    def create(cls, username):
        existing_user = cls.find_by_username(username)
        if existing_user:
            raise Exception("Username already exists. Please choose a different username.")

        user = User(username)
        CURSOR.execute(f"""
            INSERT INTO users (username)
            VALUES ('{user.username}')
        """)
        new_user_id = CURSOR.execute('SELECT last_insert_rowid() FROM users').fetchone()[0]
        CONN.commit()
        return cls.find_by_id(new_user_id)

    @classmethod
    def find_by_id(cls, id):
        if type(id) == int and id > 0:
            sql = f"SELECT * FROM users WHERE id = {id}"
            new_user = CURSOR.execute(sql).fetchone()
            if new_user:
                return cls.db_into_instance(new_user)
            else:
                raise Exception("Could not find User with that ID.")
        else:
            raise Exception("ID entered must be an integer greater than 0.")

    @classmethod
    def find_by_username(cls, username):
        if type(username) == str and len(username) > 0:
            sql = f"SELECT * FROM users WHERE username = '{username}'"
            user = CURSOR.execute(sql).fetchone()
            if user:
                return cls.db_into_instance(user)
            else:
                return None
        else:
            raise Exception("Username must be a non-empty string.")

    @classmethod
    def all(cls):
        sql = "SELECT * FROM users"
        users = CURSOR.execute(sql).fetchall()
        return [cls.db_into_instance(user) for user in users]

    @classmethod
    def db_into_instance(cls, user):
        return User(user[1], user[0])

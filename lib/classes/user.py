from . import CONN, CURSOR 

class User:

    def __init__(self,  first_initial, last_initial, id=None):
        self.first_initial = first_initial
        self.last_initial = last_initial
        self.id = id

    @property
    def first_initial(self):
        return self._first_initial
    
    @first_initial.setter
    def first_initial(self, initial):
        if type(initial) is str and len(initial) == 1:
            self._first_initial = initial
        else: 
            raise Exception("First initial must be a string and equal 1 character")
        
    @property
    def last_initial(self):
        return self._last_initial
    
    @last_initial.setter
    def last_initial(self, initial):
        if type(initial) is str and len(initial) == 1:
            self._last_initial = initial
        else: 
            raise Exception("Last initial must be a string and equal 1 character")


    def update_user_wpm(self, wpm):
        pass

    def update_user_acc(self, acc):
        pass

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                first_initial TEXT,
                last_initial TEXT
            )
        """
        )
        print("Table creation attempted. Please check your console")

    @classmethod
    def create(cls, first_initial, last_initial):
        user = User(first_initial, last_initial)
        CURSOR.execute(f"""
                INSERT INTO user(first_initial, last_initial)
                VALUES ('{user.first_initial}', '{user.last_initial}')
            """
        )
        new_user_id= CURSOR.execute( 'SELECT last_insert_rowid() FROM user').fetchone()[0]
        return cls.find_by_id(new_user_id)

    @classmethod
    def find_by_id(cls, id):
        if type(id) is int and id > 0:
            sql = f"SELECT * FROM user WHERE id= {id}"
            new_user= CURSOR.execute(sql).fetchone()
            if new_user :
                return cls.db_into_instance(new_user)
            else :
                raise Exception("Could not find User with that ID.")
        else :
            raise Exception ("ID entered must be an integer greater than 0.")
        
    @classmethod
    def find_by_name(cls, name):
        if type is str and len(name) > 0 :
            sql = f"SELECT * FROM user where first_initial LIKE '{name}' OR last_initial LIKE '{name}'"
            users = CURSOR.execute(sql).fetchall()
            if users:
                return [cls.db_into_instance(user)for user in users]
            else: 
                raise Exception("Could not find any users with that name.")
        else:
            raise Exception ('Name must be a string greater than 0 characters')


    @classmethod
    def all (cls):
        sql ="SELECT * FROM user"

        users = CURSOR.execute(sql).fetchall()
        return [cls.db_into_instance(user) for user in users]
    
    @classmethod
    def db_into_instance (cls, user):
        return User(user[1], user[2], user[0])
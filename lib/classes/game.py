from . import CONN, CURSOR 
from time import sleep
import ipdb

class Game:
    pass

    def __init__(self, user, words):
        self._user = None
        self._words = []

        self.set_user(user)

    def start_game(self):
        
        for i in range(60, 0, -1):
            print(f"Time Remaining: {i}", "\r", end="")
            attempt = input()
            # attempt = input("")
            sleep(1)


    ipdb.set_trace()

    def get_user(self):
        return self._user

    def set_user(self, user):
        from classes.user import User
        if isinstance(user, User):
            self._user = user
        else:
            raise Exception("User must be of type User")

    def get_words(self):
        return self._words
    
    def set_words(self):
        pass
    
    user = property(get_user, set_user)
    words = property(get_words, set_words)
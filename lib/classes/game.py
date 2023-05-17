# from . import CONN, CURSOR 
from time import sleep, time
from threading import Thread
import os
import sys

import ipdb

class Game:
    pass

    def __init__(self, user, words):
        self._user = None
        self._words = []

        self.set_user(user)

    def start_game(self):
        def clear_screen():
            if os.name == "nt":
                os.system("cls")  # For Windows
            else:
                os.system("clear")  # For Linux and macOS

        def user_input(timeout=60):
            inputs = []
            end_time = time() + timeout

            def input_thread():
                nonlocal inputs
                nonlocal end_time
                while time() < end_time:
                    user_input = input()
                    inputs.append(user_input)
                    # clear_screen()
                    # print(f"Seconds remaining: {max(0, int(end_time - time()))}")
                    
            input_thread = Thread(target=input_thread)
            input_thread.start()

            while input_thread.is_alive() and time() < end_time:
                remaining_seconds = max(0, int(end_time - time()))
                clear_screen()
                # print(f"Seconds remaining: {remaining_seconds}")
                print(f"Seconds remaining: {remaining_seconds}", end="\n", flush=True)
                
                sleep(1)

            clear_screen()
            if remaining_seconds == 0:
                print("Input timeout reached.")
                sleep(1)
            print()
            input_thread.join(timeout)

            return inputs
        
        user_inputs = user_input(timeout=60)
        print("User inputs:", user_inputs)

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
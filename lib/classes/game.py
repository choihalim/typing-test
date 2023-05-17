# from . import CONN, CURSOR 
from time import sleep, time
from threading import Thread
import os
import requests
import json

class Game:

    def __init__(self, user):
        self._user = None
        self._words = []

        self.set_user(user)
        self.set_words(self.generate_words())

    # generates list of ten words
    def generate_words(self):
        words = []
        api_url = 'https://api.api-ninjas.com/v1/randomword'
        for _ in range(10):
            response = requests.get(api_url, headers={'X-Api-Key': 'PF/hqSpAr1VyOEOUwNwYaA==HUK817VPrQuOaZgA'})
            if response.status_code == requests.codes.ok:
                parsed_data = json.loads(response.text)
                word = parsed_data["word"]
                words.append(word)
            else:
                print("Error:", response.status_code, response.text)
        return words
    
    def calculate_wpm(self, attempted_words):
        count = 0
        for word in attempted_words:
            if word != "" and len(word) > 1:
                count += 1
        return count
    
    def calculate_acc(self, attempted_words):
        copy_words = self._words[:]
        total_words = len(attempted_words)
        if len(attempted_words) < len(copy_words):
            copy_words = copy_words[:len(attempted_words)]
        
        matching_elements = sum(1 for x, y in zip(attempted_words, copy_words) if x == y)
        accuracy = matching_elements / total_words * 100
        
        return f"{str(accuracy)} %"

    def start_game(self):
        def clear_screen():
            if os.name == "nt":
                os.system("cls")  # For Windows
            else:
                os.system("clear")  # For Linux and macOS

        def user_input(timeout=10):
            inputs = []
            index = 0
            end_time = time() + timeout

            def input_thread():
                nonlocal inputs
                nonlocal end_time
                nonlocal index
                while time() < end_time:
                    word = self._words[index]
                    remaining_seconds = max(0, int(end_time - time()))
                    print(f"\rSeconds remaining: {remaining_seconds}\n\n{word}: ", end="")
                    user_input = input()
                    inputs.append(user_input)
                    index += 1
                    clear_screen()
            
            input_thread = Thread(target=input_thread)
            input_thread.start()

            while input_thread.is_alive() and time() < end_time:
                clear_screen()
                remaining_seconds = max(0, int(end_time - time()))
                print(f"\rSeconds remaining: {remaining_seconds}\n\n{self._words[index]}: ", end="", flush=True)
                sleep(1)
            
            clear_screen()
            star_line = "*" * 50
            print(star_line)
            print("Game Finished!")
            print(star_line)
            print()

            input_thread.join(1)

            return inputs
        
        user_inputs = user_input(timeout=5)

        # calculate score here
        # print("User inputs:", user_inputs)
        dot_line = "-" * 50
        print(f"User: {self._user.first_initial}{self._user.last_initial}\n\nScore:")
        print(dot_line)
        print("WPM: ", self.calculate_wpm(user_inputs))
        print("Accuracy: ", self.calculate_acc(user_inputs))

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
    
    def set_words(self, words):
        self._words = words
    
    user = property(get_user, set_user)
    words = property(get_words, set_words)
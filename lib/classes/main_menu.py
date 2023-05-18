from simple_term_menu import *

from score import Score
from user import User
from game import Game
from tqdm import tqdm
from time import sleep
from colorama import Fore, Style

# to run: python3 lib/classes/main_menu.py

class MainMenu:
    User.create_table()
    Score.create_table()
    
    options = ["[s] Start Game", "[c] Create User", "[v] View Scores", "[q] Quit"]
    menu_title = "\nWelcome to Typing Test! Please select an option below.\n"
    menu_cursor = "> "
    menu_cursor_style = ("fg_red", "bold")
    menu_style = ("bg_blue", "fg_yellow")

    mainMenu = TerminalMenu(
        menu_entries = options,
        title=menu_title,
        menu_cursor=menu_cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
    )

    score_options = ["[s] Show All Scores", "[f] Find Score by Username", "[r] Return to Main Menu"]
    score_submenu = TerminalMenu(
        score_options,
        title="\nScores Menu\n",
        menu_cursor=menu_cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
    )

    user_options = ["[s] Start Game", "[r] Return to Main Menu"]
    user_submenu = TerminalMenu(
        user_options,
        title="\nUsers Menu\n",
        menu_cursor=menu_cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
    )

    def progress_bar():
        num_iterations = 10
        custom_format = (
            f"{Fore.GREEN}Starting game...{Style.RESET_ALL} "
            "{desc}: {percentage:3.0f}%|"
            "{bar:20}"
            "| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
        )
        progress_bar = tqdm(total=num_iterations, bar_format=custom_format)
        for i in range(num_iterations):
            sleep(0.5)
            progress_bar.update(1)
        progress_bar.close()
        print(f"{Fore.GREEN}Game started!{Style.RESET_ALL}")

    def print_scores(scores):
        dot_line = "-" * 50
        print(dot_line)
        print("[ USER | WPM | ACCURACY | DATE ]")
        if scores:
            for score in scores:
                user = User.find_by_id(score[1])
                username = user.username if user else "Unknown User"
                print(f"{username} | {score[2]} | {score[3]} | {score[4]}")
        else:
            print("No scores available yet...")
        print(dot_line)

    quitting = False

    while quitting == False:
        options_index = mainMenu.show()
        options_choice = options[options_index]

        if options_choice == "[q] Quit":
            quitting = True
            print("\nGoodbye! Thanks for playing.\n")

        if options_choice == "[s] Start Game":
            print(f"{Fore.RED}\nPlease create a user before you start the game.{Style.RESET_ALL}")
        
        if options_choice == "[c] Create User":
            ask_username = input("Please enter a username greater than 5 characters: ")
            existing_user = User.get_user_by_username(ask_username)
            if existing_user:
                print(f"Welcome back, {ask_username}!")
                user = existing_user
            else:
                user = User.create(ask_username)
                print(f"{Fore.GREEN}User {user.username} has been created...{Style.RESET_ALL}")

            user_index = user_submenu.show()
            user_choice = user_options[user_index]
            if user_choice == "[s] Start Game":
                progress_bar()
                game = Game(user)
                game.start_game()

        if options_choice == "[v] View Scores":
            score_index = score_submenu.show()
            score_choice = score_options[score_index]
            if score_choice == "[s] Show All Scores":
                print_scores(Score.all())
            if score_choice == "[f] Find Score by Username":
                score_ask_username = input("Please enter the username: ")
                existing_user = User.get_user_by_username(score_ask_username)
                if existing_user:
                    print(f"\nScores for {score_ask_username}:\n")
                    print_scores(Score.find_by_username(score_ask_username))
                else:
                    print(f"{Fore.RED}\nUser not found. Please check that you have created user {score_ask_username}.{Style.RESET_ALL}")


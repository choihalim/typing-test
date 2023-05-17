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

    # menu_title = f"{Fore.YELLOW}Welcome to Typing Test!{Style.RESET_ALL} {Fore.YELLOW}Please select an option below.{Style.RESET_ALL}"
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
        # clear_screen=True,
    )

    score_options = ["[s] Show All Scores", "[r] Return to Main Menu"]
    score_submenu = TerminalMenu(
        score_options,
        title="Scores",
        menu_cursor=menu_cursor,
        menu_cursor_style=menu_cursor_style,
        menu_highlight_style=menu_style,
        cycle_cursor=True,
    )

    user_options = ["[s] Start Game", "[r] Return to Main Menu"]
    user_submenu = TerminalMenu(
        user_options,
        title="User",
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

    def print_scores():
        dot_line = "-" * 50
        print(dot_line)
        print("[ USER | WPM | ACCURACY | DATE ]")
        if Score.all():
            for score in Score.all():
                print(", ".join(str(item) for item in score))
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
            print("\nPlease create a user before you start the game.")
        
        if options_choice == "[c] Create User":
            ask_username = input("Please enter a username greater than 5 characters: ")
            user = User.create(ask_username)
            print(f"User {user} has been created...")

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
                print_scores()      

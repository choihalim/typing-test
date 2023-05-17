from simple_term_menu import *

from score import Score
from user import User

# to run: python3 lib/classes/main_menu.py

class MainMenu:
    
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
        # clear_screen=True,
    )

    score_options = ["Show All Scores", "Return to Main Menu"]
    score_submenu = TerminalMenu(score_options, title="Scores")

    user_options = ["[s] Start Game", "Return to Main Menu"]
    user_submenu = TerminalMenu(user_options, title="User")

    def print_scores():
        dot_line = "-" * 50
        print(dot_line)
        print(f"{Score.all()}")
        print(dot_line)


    quitting = False

    while quitting == False:
        options_index = mainMenu.show()
        options_choice = options[options_index]

        if options_choice == "[q] Quit":
            quitting = True

        if options_choice == "[s] Start Game":
            print("Please create a user before you start the game.")
            # Call Game() if User is created
        
        if options_choice == "[c] Create User":
            ask_username = input("Enter a username: ")
            print(ask_username)

            user_index = user_submenu.show()
            user_choice = user_options[user_index]
            if user_choice == "[s] Start Game":
                print("starting game")   

        if options_choice == "[v] View Scores":
            score_index = score_submenu.show()
            score_choice = score_options[score_index]
            if score_choice == "Show All Scores":
                print_scores()      

        else:
            print(options_choice)
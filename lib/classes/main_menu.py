from simple_term_menu import TerminalMenu

# to run: python3 lib/classes/main_menu.py

class MainMenu:
    
    options = ["[s] Start Game", "[c] Create User", "[v] View Scores", "[q] Quit"]

    menu_title = "Welcome to Typing Test! Please select an option below.\n"
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
        clear_screen=True,
    )

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
            print("Call the User Class")
            # Call User Class to make User and set it to the Game

        if options_choice == "[v] View Scores":
            print("Print the User Table")
            # Call Scores to print current scores 

        else:
            print(options_choice)
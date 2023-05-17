from classes.game import Game
from classes.user import User
from classes.score import Score

User.create_table()
Score.create_table()


u1 = User.create("h", "c")
g1 = Game(u1)
Game.start_game(g1)
import ipdb
from faker import Faker

from classes.user import User
from classes.game import Game

faker = Faker()

User.create_table()
Game.start_game("hello")

for n in range(0,5):
    User.create(faker.first_name()[0], faker.last_name()[0])

if __name__ == '__main__':
    print("HELLO! :) let's debug")

import ipdb;  ipdb.set_trace()

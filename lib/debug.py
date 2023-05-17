import ipdb
from faker import Faker

from classes.user import User
from classes.game import Game
from classes.score import Score

faker = Faker()

User.create_table()
Score.create_table()
Game.start_game("hello")

for n in range(0, 5):
    User.create(faker.first_name()[0], faker.last_name()[0])

def create_fake_score():
    user_id = faker.random_int(min=1, max=5)  # Generate a random user ID
    wpm = faker.random_int(min=50, max=100)  # Generate a random WPM between 50 and 100
    accuracy = faker.random_number() * 100  # Generate a random accuracy percentage
    date = faker.date_between(start_date='-1w', end_date='today')  # Generate a random date within the past week

    score = Score.create(user_id, wpm, accuracy, date)
    return score

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    # Create a fake score
    fake_score = create_fake_score()
    print(fake_score)

    ipdb.set_trace()


import ipdb

from classes.User import User
faker= Faker()

User.create_table()

for n in range(0,5):
    User.create(faker.first_initial(), faker.last_initial())

if __name__ == '__main__':
    print("HELLO! :) let's debug")

import ipdb;  ipdb.set_trace()

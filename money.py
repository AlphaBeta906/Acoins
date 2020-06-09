from random import randint
from time import sleep
money = 0
while True:
    c = randint(1, 2)
    if c == 1:
        people = "Miner " + str(randint(1, 9999999))
    else:
        people = "User " + str(randint(1, 9999999))
    chance = randint(1, 99999990)
    if chance == 1:
        resiver = "You"
        money_lost = randint(1, 1000)
    else:
        cu = randint(1, 2)
        if cu == 1:
            resiver = "Miner " + str(randint(1, 9999999))
        else:
            resiver = "User " + str(randint(1, 9999999))
        money_lost = randint(1, 10000)
    if c == 1:
        co = randint(1, 2)
        if co == 1:
            say = people + " gets " + str(money_lost) + " acoins"
            money += money_lost
        else:
            say = people + " pays " + str(money_lost) + " acoins to " + resiver
    else:
        say = people + " pays " + str(money_lost) + " acoins to " + resiver
    print (say)
    sleep(1)

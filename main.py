# WELCOME TO MY PROGRAM
# for any question, ask at mycn18.dev@gmail.ocm

import random
import time

def preview():
    print("Hi ! Welcome to my thimble random game !")
    time.sleep(1)
    print("It's a very simple game, where you lanch two thimbles, and your goal is to make a score upper than the IA")
    time.sleep(1)
    print("To be honest, this is a base for other programs... but also nice to play ^^")
    time.sleep(1)
    print("So, are you ready?")
    input("--> ")

    game_start()

def game_start():
    print("\nFine ! lets begin the game...")
    time.sleep(1)
    pritn("IA is building the thimbles...")
    time.sleep(2)

    # building the thimbles:
    exits = [1, 2, 3, 4, 5, 6]
    retry = True
    round = 1

    while retry:
        print("-- round " + str(round) + " --")
        time.sleep(1)
        print("\nLaunch the thimbles !")
        input("--> ")
        time.sleep(1)
        score_player = exits[random.randint(0, 5)] + exits[random.randint(0, 5)]
        print("thimbles are rolling...")
        time.sleep(2)
        print("You made", score_player, '!')
        time.sleep(1)
        print("It's IA turn...")
        time.sleep(2)
        IA_score = exits[random.randint(0, 5)] + exits[random.randint(0, 5)]
        print("IA made", IA_score, '!')
        time.sleep(1)
        print("...")
        time.sleep(1)

        if score_player > IA_score:
            print("IA won ^^")
        elif score_player < IA_score:
            print("You won...")
        else:
            print("It's draw ! Incredible...")
        
        time.sleep(1)
        print("Do you want to retry? (Y/n)")
        retry = input("--> ")
        pos = ['Y', 'n']
        while not(retry in pos):
            print("Bad answer ^^")
            retry = input("retry --> ")
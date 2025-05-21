# Rock Paper Scissors Game In Python

# IMPORTING REQUIREMENTS...

import random
import time
import sys

#  INITIALIZING VARIABLES

ini = 0
rock = 1
paper = 2
scissors = 3

names = {rock:'Rock', paper:'Paper', scissors:'Scissors'}

# DEFINING GAME RULES

rules = {rock:scissors, paper:rock, scissors:paper} # Rock dominates the scissors...

# STORING THE SCORES

player_score = 0
computer_score = 0

# Initializing the Game...

def start():
    print('Welcome to Rock Paper Scissors...')

    while game(): pass
    scores()

def game():

    # global player, computer

    player = move()
    computer = random.randint(1,3)

    # Getting the winner
    results(player, computer)

    if player != 0:
        return play_agian()

def initialize():

    global ini
    ini += 1

    print('\nChoose from the following - ')
    print('Rock - 1')
    print('Paper - 2')
    print('Scissors - 3')
    print('Current Score - 4')
    print('Quit The Game - 0')

def move():

    while True:

        if ini == 0: initialize()

        player = int(input('\nYou Choose? - '))

        if player in [0,1,2,3,4]:
            return player
        else:
            print('Invalid Input')

def results(player, computer):

    if player == 4:
        scores()
        return

    global player_score, computer_score

    if player not in [0,4]:

        print('\nYou choose - ',names[player])
        print('Computer threw -',names[computer])

        if player == computer:
            print('\nThe Game is Tie!')

        elif player != computer:
            if rules[player] == computer:
                print('\nYou won this one! Ah Finally')
                player_score += 1

            else:
                print('\nEven Computer is more luckier than YOU! Hah!')
                computer_score += 1

        time.sleep(2)

def play_agian():

    game()

    # get = input('\nDo You wanna play again? - ')
    # if get in ['y']:
    #     return get
    # else:
    #     sys.exit

def scores():

    global player_score, computer_score

    # print('\nHigh Scores - ')
    print(f'\nPlayer Won {player_score} matches.')
    print(f'Computer Won {computer_score} matches.')

    time.sleep(1)


if __name__ == '__main__': # Only execute following code if the file is directly executed, not when imported as a module 
    start()

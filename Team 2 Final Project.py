#Names: Gabriel Piccolella, Gage Huntington, Ryley Ashcraft, Eric Lin.
#Team: 2
#Class: 5th Hour
#Assignment: Final Project
#Scrum master doc https://docs.google.com/document/d/1AWQLpbUFunfXm0-jOgXlLe1Y2ZyS0_uu7FVCA9zDAnc/edit?pli=1&tab=t.0





import random
import time

x = 0

def system2():
    global x
    while not x == 1:
        dice3 = random.randint(1, 6)
        dice4 = random.randint(1, 6)
        print(f"You Rolled a {dice3} and a {dice4}")
        time.sleep(1.5)
        if dice3 + dice4 == 7:
            print("7 Rolled, Game Over!")
            playNY()

        elif dice1 + dice2 == dice3 + dice4:
            print(f"{dice3 + dice4} Rolled Again, You Win!!!!")
            x += 1

        else:
            print("Nothing Rolled, Go Again")
            system2()

def system():
    print(f"You Rolled a {dice1} and a {dice2}")

    if dice1 + dice2 == 7 or dice1 + dice2 == 11:
        print("You Rolled A Natural!")
        print(f"Double Initial Bet of {first_bet}")

    else:
        if dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
            print(f"{dice1+dice2}Rolled, Game Over")
            playNY()

        else:
            print("Nothing Rolled, Continue on")
            time.sleep(1.5)
            system2()

def bet_numb():
    try:
        global first_bet
        first_bet = int(input("What Is Your Initial Bet?   :"))
        system()

    except ValueError:
        print("Not Valid Answer, Try Again.")
        bet_numb()

def dice_roll():
    global dice1
    global dice2
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    bet_numb()

def playNY():
    player = input("Would you Like to Start the Game?   :")

    if player == "y" or "Y" or "Yes" or "yes":
        print("Welcome to Craps")
        dice_roll()

    elif player == "n" or "N" or "No" or "no":
        print("Goodbye")
        exit()

    else:
        print("Not Valid Answer, Try Again.")
        playNY()

def begining():
    print("Welcome to street craps! Here's how you play")
    time.sleep(2)
    print("First you will enter a bet, there are more rules for craps but for now we will be playing street craps")
    time.sleep(3)
    print("In street craps you place a bet on whether you roll a 7 or 11, if you roll either of these numbers, you win!")
    time.sleep(3)
    print("If you roll a 2,3 or 12 you lose automatically and all money is forfeited.")
    time.sleep(2)
    print("If you roll none of these numbers, then you roll once more, on your second roll you do NOT want a 7")
    time.sleep(3)
    print("Instead you want to roll a 4,5,6,8,9 or 10, you then roll until you get one of these numbers or a 7")
    time.sleep(3)
    print("Then you restart the process until you run out of money.")
    time.sleep(2)
    playNY()

begining()
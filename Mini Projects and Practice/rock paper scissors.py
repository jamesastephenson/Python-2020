#Rock Paper Scissors
#This should be a basic game of Rock Paper Scissors against the computer
#The player should be asked for input and then the program should respond

#begin by opening the randint library
from random import randint

#this list gives a series of options
play_options = ["Rock", "Paper", "Scissors"]
#by setting the randint with the play_options list, we can use that result
#this avoids having to do weird number conversions
computer_move = play_options[randint(0, 2)]

#setting player to false, when they win it will switch to True
player = False

#we set a while loop to continue until the player wins
while player == False:
    #this is where the player is asked to input their move
    player_move = input("Choose Rock, Paper, or Scissors: ")
    #each if and elif statement accounts for different game outcomes
    if player_move == computer_move:
        print("This match was a draw!")
        elif player_move == "Rock":
        if computer_move == "Paper":
            print("The computer uses paper to cover your rock. You lose.")
        else:
            print("You smash the computer\'s scissors with your rock! You win!")
            print("You have defeated the computer and may now destroy its kingdom.")
            player = True
    elif player_move == "Paper":
        if computer_move == "Scissors":
            print("The computer cuts your paper with its scissors. You lose.")
        else:
            print("You cover the computer\'s rock with your paper! You win!")
            print("You have defeated the computer and may now destroy its kingdom.")
            player = True
    elif player_move == "Scissors":
        if computer_move == "Rock":
            print("The computer smashes your scissors with its rock. You lose.")
        else:
            print("You cut the computer\'s paper with your scissors! You win!")
            print("You have defeated the computer and may now destroy its kingdom.")
            player = True
    #this else statement prevents errors from putting something irrelevant to the game
    else:
        print("That is not a valid input for this game. Please input \"Rock\", \"Paper\", or \"Scissors\".")

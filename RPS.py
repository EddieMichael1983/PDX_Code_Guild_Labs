
import random

rps = ['rock', 'paper', 'scissors']  #defining random values for the computer to choose from


user_choice2 = 'y'  #this sets the program up to run again later when the user is asked if they want to play again
while user_choice2 == 'y':  #while user_choice2 == y is TRUE the program keeps going

    user_choice = input('Choose rock, paper, or scissors: ') #the computer asks the user for their choice

    choice = random.choice(rps) #the computer randomly chooses rock, paper, or scissors
    print(f'The computer chose {choice}.')

    if user_choice == 'rock' and choice == 'rock':
        print('Tie')
    elif user_choice == 'rock' and choice == 'paper':
        print('Paper covers rock, you lose.')
    elif user_choice == 'rock'and choice == 'scissors':
        print('Rock smashes scissors, you win.')
    elif user_choice == 'paper' and choice == 'rock':
        print('Paper covers rock, you win.')
    elif user_choice == 'paper' and choice == 'paper':
        print('Tie')
    elif user_choice == 'paper' and choice == 'scissors':
        print('Scissors cuts paper, you lose.')
    elif user_choice == 'scissors' and choice == 'rock':
        print('Rock smashes scissors, you lose.')
    elif user_choice == 'scissors' and choice == 'paper':
        print('Scissors cuts paper, you win.')
    elif user_choice == 'scissors' and user_choice == 'scissors':
        print('Tie')     #determines who won and tells the user


    user_choice2 = input('Do you want to play again?: y/n ')

#Guess the number

import random
num1 = random.randint(1,10)

counter = 1  #counter set at 1 because user will guess at least one time

while True:

    user_guess = input("Guess what number between 1 and 10 I'm thinking of?: ")
    user_guess = int(user_guess)

    if user_guess == num1:
        print("You got it!")
        break
    counter = counter + 1

    if user_guess > num1:
        print("Too high!")

    elif user_guess < num1:
        print("Too low!")

    if counter > 5 and user_guess != num1:   #allows the user 5 maximum guesses
        print("You lost. Game Over.")
        break
print(f"You guessed {counter} times.")


#Tell the user whether their current guess is closer than their last.

#Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.

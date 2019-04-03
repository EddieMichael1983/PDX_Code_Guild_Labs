#favorite_colors.py
import os
favorite_color_list = []
while True:
    user_color = input("Give me a favorite color or (done):")
    if user_color == 'done':
        break
    favorite_color_list.append(user_color)
os.system('clear')  #on WINDOWS use: os.system('cls')

color_guesses = []

while len(color_guesses) < len(favorite_color_list):
    user_guess = input(f"Guess one of my {len(favorite_color_list)} favorite colors: ").lower
    color_guesses.append(user_guess)
favorite_color_list.sort()
color_guesses.sort()
print(favorite_color_list)
print(color_guesses)
if favorite_color_list == color_guesses:
    print("Correct!")
else:
    print("Nice Try")

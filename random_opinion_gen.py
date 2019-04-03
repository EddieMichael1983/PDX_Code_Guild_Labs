#random_opinion_gen.py
import random
user_movie = input("What movie do you like?: ")
opinion = random.choice(['good', 'bad', 'okay','horrible'])
print(f"I thought that movie was {opinion}.")
if opinion == 'good' :
        print("Great choice!")
        

#turn_direction.py
import random
direction_list = ["North", "East", "South", "West"]
user_direction = random.randint(0,3)
print(f"You are facing {direction_list[user_direction]}")
left_right = input("Turn left or right: ")
if left_right == 'left':
    dir = -1
else:
    dir = 1
user_turns = int(input("How many turns: "))
user_direction = user_direction + dir * user_turns
print(f"You are facing {direction_list[user_direction % 4]}")

# enough_sleep.py
user_sleep = input("How many hours did you sleep last night?: ")
user_sleep = int(user_sleep)
if user_sleep <= 6:
    print("Get more sleep")
if user_sleep >= 10:
    print("Wake up, sleepy head")
if user_sleep >= 7 and user_sleep <= 9:
    print("Perfect")

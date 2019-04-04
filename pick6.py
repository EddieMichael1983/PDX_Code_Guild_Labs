import random

def pick6():
    numbers = [(random.randint(1, 99)), (random.randint(1, 99)), (random.randint(1, 99)), (random.randint(1, 99)), (random.randint(1, 99)), (random.randint(1, 99))]
    #Return 6 random numbers in a list
    return numbers
print(pick6())

def matches(winning_ticket, current_ticket):
 
    for i in range(len(winning_ticket)):
        print(winning_ticket[i], current_ticket[i])
  
# #     #Return the number of the matches
# #     #AKA return an integer that is the number of matches

def play_pick6():
    balance = 0 
    for k in range(100,000):
        print(winning_ticket, current_ticket)


ticket_cost = 2

if matches == 1: 
    winnings = 4
elif matches == 2:
    winnings = 7
elif matches == 3:
    winnings = 100
elif matches == 4:
    winnings = 50,000
elif matches == 5:
    winnings = 1,000,000
elif matches == 6:
    winnings = 25,000,000

winnings + ticket_cost = new_balance

# # # #tests
# winning_ticket = pick6()
# print(x)

m = matches([25, 10, 1, 2, 5, 9], [25, 9, 1, 2, 5, 9])
print(m) #The value should be 5
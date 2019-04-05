import random

<<<<<<< HEAD

def pick6():

    my_ticket = []

    for count in range(6):
        my_ticket.append(random.randint(1,99))
    
    return my_ticket

def matches(winning_ticket, my_ticket):
    counter = 0
 
    for i in range(len(winning_ticket)):
        if winning_ticket[i] == my_ticket[i]:
            counter = counter + 1  

    return counter
  
def play_pick6():
    balance = 0 
    winnings = 0
    winning_ticket = pick6()
    
    for i in range(100000):
        my_ticket = pick6()
        matching_numbers = matches(winning_ticket, my_ticket)

        balance = balance + 2

        if matching_numbers == 1: 
            winnings += 4
        elif matching_numbers == 2:
            winnings += 7
        elif matching_numbers == 3:
            winnings += 100
        elif matching_numbers == 4:
            winnings += 50000
        elif matching_numbers == 5:
            winnings += 1000000
        elif matching_numbers == 6:
            winnings += 25000000

    return_on_investment = winnings - balance

    print(f"Money spent ${balance}\n Money won ${winnings}\nReturn on Investment = {return_on_investment}")

play_pick6()



=======
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
>>>>>>> 14b4082ab068489c066936250e7b331265ca1591

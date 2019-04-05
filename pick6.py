import random


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




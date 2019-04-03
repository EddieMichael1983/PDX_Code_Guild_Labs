#make_change.py
unconverted_pennies = input("Enter an amount of money in pennies:  E.G. 136 for $1.36: ")
unconverted_pennies = int(unconverted_pennies)

quarters = unconverted_pennies // 25
unconverted_pennies = unconverted_pennies % 25
dimes = unconverted_pennies // 10
unconverted_pennies = unconverted_pennies % 10
nickels = unconverted_pennies // 5
unconverted_pennies = unconverted_pennies % 5


print(f'{quarters} quarters')
print(f'{dimes} dimes')
print(f'{nickels} nickels')
print(f'{unconverted_pennies} pennies')


#unconverted_pennies = float(input("How much money: ")) * 100
#How much Money: 1.36
#unconverted pennies = round(unconverted_pennies)

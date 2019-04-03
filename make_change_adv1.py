#make_change.py
unconverted_pennies = float(input("How much money? Use a decimal and no dollar sign. EG 7.48 for $7.48: ")) * 100
unconverted_pennies = round(unconverted_pennies)

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

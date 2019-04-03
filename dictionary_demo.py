# fruits = ['apple', 'banana', 'guava']
# nums = [1, 2, 3]
#
# for fruit in fruits:
#     print(fruit)
#
# for num in nums:
#     print(num)


prices = {'apple': 1.5, 'banana': 1, 'guava': 3}

print(prices['apple'])

values = list(prices.values())

for key in prices:
    print(f'{key} {prices[key]}')
    if prices[key] == 1.5:
        print(key)

nums = []

while True:
    value = input('Enter a number, or done: ')
    if value == 'done':
        break
    nums.append(value)

print('You entered: ' + str(nums))

runningSum = 0  #defines a variable called runningSum

for num in nums:            
    runningSum += int(num)       
print ('The total is: ' + str(runningSum))          

average = runningSum / len(nums)   #defines our average of nums as running sum divided by length of list
print('The average is: ' + str(average))   


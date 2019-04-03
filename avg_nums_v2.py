nums = [] #sets up list of numbers

while True:    #user enters values until done
    
    value = input('Enter a number, or done: ')
    if value == 'done':
        break
    nums.append(float(value))   #users entries to list each time
                                #use float instead of int to account for decimal points

print('You entered: ' + str(nums))

runningSum = 0  #defines a variable called runningSum
for num in nums:  #using a for loop to iterate over every num
    runningSum += float(num) #adds value 'num' to the running sum
print ('The total is: ' + str(runningSum))  #prints the running sum        

average = runningSum / len(nums)   #defines our average of nums as running sum divided by length of list
print('The average is: ' + str(average))  #prints the average of the nums




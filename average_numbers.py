#average numbers lab 10

nums = [5, 0, 8, 3, 4, 1, 6]  #start with the following list

runningSum = 0  #defines a variable called runningSum

for num in nums:            #using a for loop to iterate over every num
    runningSum += num       #adds value 'num' to the running sum
print(runningSum)           #prints the running sum

average = runningSum / len(nums)   #defines our average of nums as running sum divided by length of list
print(average)                      #prints the average of the nums


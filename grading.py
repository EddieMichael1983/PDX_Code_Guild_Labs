#grading.py
user_grade = input("Enter a number representing your student\'s grade: ")
user_grade = int(user_grade)

if user_grade == 100:
    print ('A+')
elif user_grade > 89 and user_grade <100:
    print ('A', end = '')
elif user_grade > 79 and user_grade <= 89:
    print ('B', end = '')
elif user_grade > 69 and user_grade <= 79:
    print ('C', end = '')
elif user_grade > 59 and user_grade <= 69:
    print ('D', end= '')
elif user_grade <= 59:
    print ('F')

if user_grade % 10 >= 7:
    print('+')

if user_grade % 10 <=3:
    print('-')

import random
rival_score = random.randint(0,100)
print (f'Your rival\'s score was {rival_score}')

if rival_score < user_grade:
    print ('You scored higher than your rival.')
elif rival_score > user_grade:
    print ('Your rival scored higher than you.')

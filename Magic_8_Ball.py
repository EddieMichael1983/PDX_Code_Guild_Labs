print('welcome!')
import random
user_question = input("Ask the eight ball a yes or no question: ")
answer = random.choice(['yes', 'no', 'maybe', 'ask again later'])
print(answer)
user_question2 = input("Do you want to ask a second question? Enter yes or no: ")
if answer == 'yes':
    user_question = input("Ask the eight ball a yes or no question: ")
    answer = random.choice(['why not','i don\'t know', 'sure', 'nope'])
    print(answer)
    print('Game Over')

if answer == 'no':
    print('Game Over')

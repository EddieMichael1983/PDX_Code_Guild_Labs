import random
eyes = [':', '8', 'x', ';']
noses = ['-', '~', 'っ', '^', '\'', '']
mouths = ['D', 'O', 'o', ')', '(', '<', 'v', 'P', '}', '{']

while True:

    eye = random.choice(eyes)   #insert random.choice values into the loop
    nose = random.choice(noses)
    mouth = random.choice(mouths)

    print(eye + nose + mouth)   #prints 5 random faces

    user_input = input('Would you like another emoticon? y/n')
    if user_input == 'n':
        break

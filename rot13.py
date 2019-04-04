#rot13.py

#Modulus is going to help you!

message = input("Type your message here: ")

#def rot13(message):
for character in message:  #iterates 
    #ASCII character code
    ascii_representation = ord(character)        #step 1: convert to ASCII 
    print(ord(character))

for character in message:

    ascii_plus_13 = ord(character) + 13 % 26
    print(ord(character) + 13 % 26)             #step 2: rotates ASCII code over by 13

     #Return back the rot13 string
for character in message:
    c = ord(character) % 26
    print(c)




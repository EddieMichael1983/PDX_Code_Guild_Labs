import pprint

rot13_dict = {}

for i in range(26):
    rot13_dict[chr(i + 97)] = chr(((i + 13) % 26)+ 97)

for i in range(26):
    rot13_dict[chr(i + 65)] = chr(((i + 13) % 26)+ 65)

pprint.pprint(rot13_dict)

def rot13(message):
    encrypted_message = []
    for character in message:
        try:
            encrypted_message.append(rot13_dict[character])
        except KeyError:
            encrypted_message.append(character)
      
    return ''.join(encrypted_message)

secret = rot13('I WANNA ROCK!!!!')
print(secret)
print(rot13(secret))

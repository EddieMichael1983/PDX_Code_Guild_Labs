def encode_character(ascii_code, offset):
    # Get the offset into the alphabet
    index = ascii_code - offset
    # Add 13 and wrap around with modulus 26
    index = (index + 13) % 26

    # Add our offset back, get our encoded character
    encoded_character = index + offset

    return chr(encoded_character)

def rot13(message):
    # How we store the message characters
    encrypted_message = []

    # For each character in message
    for character in message:
        # Get the ASCii code
        ascii_code = ord(character)

        # If the character is uppercase
        if ascii_code >= 65 and ascii_code < 65 + 26:
            encrypted_message.append(encode_character(ascii_code, 65))
        # If the character is lowercase
        elif ascii_code >= 97 and ascii_code < 97 + 26:
            encrypted_message.append(encode_character(ascii_code, 97)) 
        # If the character isn't in the alphabet           
        else:
            encrypted_message.append(chr(ascii_code))

    return ''.join(encrypted_message)


secret = rot13("Hello World!!!")
print(secret)
print(rot13(secret))
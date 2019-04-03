#anagram_checker

user_word1a = input("Enter a word or phrase: ").lower()
user_word2a = input("Enter a second word or phrase: ").lower()

user_word1a = user_word1a.replace(' ', '')
user_word2a = user_word2a.replace(' ', '')

user_word1 = list(user_word1a)
user_word2 = list(user_word2a)
#print(user_word1)  lines 12 -13 can be used if you want to see string characters printed out in a list
#print(user_word2)

user_word1.sort()
user_word2.sort()

if user_word1 == user_word2:
    print(f"{user_word1a} and {user_word2a} are anagrams")
else:
    print(f"{user_word1a} and {user_word2a} are not anagrams")

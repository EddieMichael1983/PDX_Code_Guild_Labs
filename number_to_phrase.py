#number_to_phrase.py
ones = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

teens = { 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}

tens = { 2 : 'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}

def number_to_phrase(number):
    tens_digit = number // 10
    ones_digit = number % 10

    if number < 10:
        return(ones[number])
    if number >= 10 and number < 20:
        return(teens[number])  
    if number >= 20:
        return(tens[tens_digit] + ones[ones_digit])  


print(number_to_phrase(97))


# tens = {2:'twenty'}
# tens[2]
# 'twenty'
# ones = { 1: 'one' }
# print(tens[2], ones[1])
# twenty one
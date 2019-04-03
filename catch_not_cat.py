#catch_not_cat.py
while True:

    import random
    pattern_list = ['##',"$$",'%%','\\\\','//','~~']
    out_string = ''
    length = 20
    width = 5
    for num in range(length):
        out_string = out_string + random.choice(pattern_list) *width
        out_string = out_string + '\n'
    print(out_string)

var1 = input("Please type cat >")
if var1 == 'cat':
    break

# va2 = bird
var2 = 'bird'
while var2 != 'bird':
    var2 = input("Please type bird >")

running = True
while running == True:
    var3 = input("Please type dolphin >")
    if var3 == 'dolphin':
        running = False

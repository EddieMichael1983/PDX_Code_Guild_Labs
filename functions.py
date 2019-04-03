#functions.py   #illustrates the difference between print and return

def noisy_add(num1, num2):
    print(f"ADDING {num1} AND {num2}!!! :D")
    return num1 + num2    #return leaves behind what it points at

def bad_add(num1, num2):
    print(num1 + num2)     #print just shows what it prints and leaves none behind

    def return4(in_thing):
        print(in_thing)
        return 4

    def print4(in_thing):
        print(4)
        return in_thing


var1 = return('ab') + return4('cd')   #running line 10 - 12
ab
cd

print var1
8

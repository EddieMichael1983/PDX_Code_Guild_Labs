#pattern_gen.py
import random
pattern_list = ['##',"$$",'%%','\\\\','//','~~']
out_string = ''
length = 20
width = 5
for num in range(length):
    out_string = out_string + random.choice(pattern_list) *width
    out_string = out_string + '\n'
print(out_string)

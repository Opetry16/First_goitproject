'''import random
l = [ "Oleh", 'Kate', "Sasha", "Max"]

res= random.choices (l, k=12)
print (res)

'''

import random

set_of_letters = ["A", "B", "C", "M"]
set_of_number  = ["2", "1", "4", "5"]
l1 = random.choices(set_of_letters, k=2)
l2 = random.choices(set_of_letters, k=2)
l3 = random.choices(set_of_number, k=4)
res = l1+l2+l3

print (l1)
print (l2)
print (l3)
print (res)

number = "".join (l1 +[" "]+l3+[" "]+l2)

print (number)

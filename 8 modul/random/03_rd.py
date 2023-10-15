import random

amount = 4
array = [1,2,3,4,8,7,123]
array_sorted = sorted (array)

print (array)
print ("*******")

attemp = 0
while array_sorted != array:
    attemp += 1
    random.shuffle(array)
    print (f"# {attemp}, arr:{array}")

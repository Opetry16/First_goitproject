import re

s = "I bought 77 nuts for 6$ and 110 bolts for 3$."

print(re.findall("[0,1,3,6,7]", s))
print(re.findall("[^0,1,3,6,7]", s))
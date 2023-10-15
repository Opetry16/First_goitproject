from collections import defaultdict

d = defaultdict (list)
value = d["Vodafone"]
value.append("0509995522")
print (d) 

sq = [i.upper () for i in ["ddffd", "adssfd0"]]
print(sq)

res = { i:i**2 for i in range (200) if i % 2 == 0}
print (res)
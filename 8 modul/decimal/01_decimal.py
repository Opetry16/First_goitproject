from decimal import Decimal, getcontext


'''# example round ()
a = round(2.1234213344, 2)
b = round(3.1239837482, 2)
res0 = a*b
print (res0)
'''

getcontext().prec = 1
a = Decimal ("0.223")
b= Decimal ("0.23232")

res=(a*b)
print (res)


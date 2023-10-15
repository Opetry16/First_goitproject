fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

res = {fruit.capitalize() if len(fruit) == 5 else fruit for fruit in fruits}

print (res)

#2
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
res = dict()
for fruit in fruits:
    res[fruit]=len(fruit)
    
print (res)

#3
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

res = {fruit : len(fruit)  for fruit in fruits}

print (res)

#4
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
for index, fruit in enumerate(fruits):
    print (fruits)
    

#5
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

res = {fruit:index for index, fruit in enumerate(fruits)}
print (res)

#6
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_dict = {'mango': 0, 'kiwi': 1, 'strawberry': 2, 'guava': 3, 'pineapple': 4, 'mandarin orange': 5}

res = {fruit : index for fruit, index in fruits_dict.items()if index %2 ==0}

print (res)
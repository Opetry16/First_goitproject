import re

def find_glasses(array):
    for word in array:
        if re.search(r'o-+o', word):
            return array.index(word)
        
data= ["o--#--o", "dusto--odust",'more dust']
print(re.search(r'o-+o', "dusto--odust" ))
print (find_glasses(data))


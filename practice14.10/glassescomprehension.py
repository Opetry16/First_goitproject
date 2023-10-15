#classis with cicles

import re

#a = [<return result> <iterate> if else ]

a = [ i**2 for i in range (100) if i > 10 and i < 20]
print (a)

#
import re

#a = [<return result> <iterate> if else ]

a = [ (i**2) if  i > 10 and i < 20 else i for i in range (100)]
print (a)

#comprehension example
import re

def find_glasses(array):
    return[word for word in array if re.search(r'o-+o', word)is not None]
        
data= ["o--#--o", "dusto--odust",'more dust']
print(re.search(r'o-+o', "dusto--odust" ))
print (find_glasses(data))
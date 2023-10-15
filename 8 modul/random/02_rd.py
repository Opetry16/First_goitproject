import random

coin = {
    1: "Orel",
    2: "Reshka"
    
}

count_O = 0
count_P= 0

sequence = list ()

while count_O < 6 and count_P < 6:
    choice = random.randint (1,2)
    if choice == 1:
        count_O += 1
        count_P = 0
    else:
        count_P += 1
        count_O += 0
    name = coin[choice]
    sequence.append (name)
print (sequence)
print (len(sequence))
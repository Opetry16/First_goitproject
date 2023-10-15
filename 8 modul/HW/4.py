from random import randrange
import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка на обмеження параметрів
    
    
    if min < 1 or max > 1000 or min >= max or quantity <= min or quantity >= max:
        return []

    numbers = random.sample(range(min, max), quantity)

    # Сортування випадкових чисел за зростанням
    numbers.sort()

    return numbers
            
            
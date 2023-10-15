
import random
import string

# Define a function to generate a random car plate
def generate_car_plate():
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    numbers = ''.join(random.choice(string.digits) for _ in range(4))
    return f'{numbers}-{letters}'

# Generate and print a random car plate
random_plate = generate_car_plate()
print("Random Car Plate:", random_plate)
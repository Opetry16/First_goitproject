import calendar 
import faker import Faker 
from constance import MENU
from exceptions import NOTinRange
from pathlib import Path

FILENAME = Path(__file__).parent / "losses.txt"
print(FILENAME)

def add_new_record (name, amount):
    with open ()

def show_statistics ():
    pass

while True:
    print(MENU)
    try:
        choice = int(input("Make your choice please"))
        if choice <1 or choice >5:
            raise NOTinRange 
    except ValueError:
        print ("pllease write option number")
        continue
    except NOTinRange:
        print("Choice from 1 to 5")
        continue
    if choice == 1:
        add_new_record ()
    elif choice == 2:
        show_statistics()
    elif choice == 3:
        print ("please enter your year")
        try:
            year = int(input(">>>>>"))
            text = calendar.calendar
            print (text)
        except ValueError:
            print ('please wrrite the year')
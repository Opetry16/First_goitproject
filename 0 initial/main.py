from math import gcd


print("Hello World", "I am very happy to start my Phython studies")
print("Hello GID")
print("Hello GOIT")
print("Hello NEW YEAR")
print("Hello NEW YEAR")# this is not true
s1 = "Hello,"
s2 = " World!"
joined_string = s1 + s2
a=2
b=3**5
P=a+b
print("Hello NEW YEAR")# this is not true
name = "Oleg"
f"Hello, {name}!"
a = 3
b = 5
c = a < b   # True
d = a > b   # False
a == b      # False
a != b      # True


'''name=input("what is our name?")
print(f"Hello {name}")
age = input("How old are you? ")

if int(age) >= 18:
    print(f"You are adult already, {name}.")
else:
    print(f"You are infant yet, {name}.")'''
   
'''a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')
    
money = input("How many money do you have?")
money=int(money)
if money > 0:
    print(f"You have {money} on your bank account")
elif money ==0:
    print("You have no money and no debts")
else:
    print("You have debt, looser! ")

user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!") '''
# This function adds two numbers

#Calculator 2.15
'''
result = None
operand = None
operator = None
wait_for_number = True
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    operand = input("Enter choice(1/2/3/4): ")
    if operator in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operator == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operator == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operator == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
          break
    else:
        print("Invalid Input")
        '''
    
    
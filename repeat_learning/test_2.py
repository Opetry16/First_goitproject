age = input("My age:")
age = int(age)
it_is_adult = age >= 18

print (it_is_adult)
if age < 18:
    age = "you need your parent"
elif age > 90:
     age = "you can really dance?"
elif age > 125:
    age = "you are the oldest one in the World) Congrats!"
else: 
    age = "You can pass"
print (age)


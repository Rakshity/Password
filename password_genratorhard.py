import string
import random

letters = string.ascii_letters
number = string.digits
charecter = string.punctuation

letter_1 = int(input("How many alphabet do you want "))
number_1 =int(input("How many Number you want "))
charecter_1 =int(input("How many Charecter you want "))

password=[]
for letter in range(0,letter_1):
    password+=random.choice(letters)
    
for chara in range(0, number_1):
    password.append(random.choice(number))
    
for x in range (0,charecter_1):
    password+=random.choice(charecter)
    
print(password)
random.shuffle(password)
print(password)

passw=""
for char in password:
    passw+=char
    
print(f"You're password is {passw}")
    
    
    

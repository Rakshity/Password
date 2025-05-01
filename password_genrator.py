python
import string 
import random 

alpha = int(input("how many letter you want"))
char = int(input ("how many char you want"))
num = int(input("how many number you want"))

alphabet_uppercase = string.ascii_letters
alphabet_n = int(len(string.ascii_letters))
print(len(alphabet_uppercase))

charecter = string.punctuation
charecter_n= len(string.punctuation)
print(type(charecter_n))

number = string.digits
numner_n= len(number)
print(len(number))


password = ""
for alpha in range (0,alpha):
    password+=random.choice(alphabet_uppercase)
    
for x in range(0,char):
    password+=random.choice(charecter)
    
for x in range (0,num):
    password+=random.choice(number)

print(f"password is {password}")


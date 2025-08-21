data_nig = 1000 #integer
data_lol = 234.45 # float
data_again = True # boolian
complex_numbers = 10 + 3j # complex number x + bi
#aricmatic expression
# 10 * 9 multiplication
# 10/5 division
# 10 % 2 modular
# 10 // 3 
# 10 **2 power
# 10 + 3 addition
# 30 - 10 substraction
# a += 3 
# a = a + 5

# func for numbs
import math
print(round(3.2))
print(abs(-2))
print(math.ceil(3.3))

#type conversion
float()
str()
int()
bool()
x_num = int(input ("x: "))
y_num = x_num + 3
print(f"x:{x_num},y:{y_num}")


data_niger = "lol i am fine." # string

#strings 
#commenting method
# 1st single comment #
"'2nd  multiple comment."
# lenth func
random_sentance = "minecraft"
print(len(random_sentance))
sentance_farm = "abcdefghijklmnopqrstuvwxyz"
a = random_sentance[0:3]
b = random_sentance[3:7]
c = random_sentance[4:]
d = random_sentance[3:8]
print(a,b,c,d)
name_production = sentance_farm[12] + sentance_farm[20] + sentance_farm[6] + sentance_farm[3] + sentance_farm[7] + sentance_farm[14]
print(name_production)

#string formating
sentance = "python programming"
print(sentance.upper())
print(sentance.lower())
print(sentance.capitalize())
print(sentance.strip())# remove the gaps from first and end.
print(sentance.rstrip())
print(sentance.lstrip())
print(sentance.title())
print(sentance.find("pro"))
print(sentance.replace("pro","nig"))
user_input = input("enter your message: ")
print(user_input.replace("bi","ni"))
if "bi" in user_input :
    print(user_input.replace("bi","nig"))
i = int(input("patern size: "))
for num in range(i):
    print("✅"*(num+1))

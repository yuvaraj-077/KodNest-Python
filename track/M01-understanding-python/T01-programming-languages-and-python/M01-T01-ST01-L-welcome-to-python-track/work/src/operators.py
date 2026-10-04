# Arithmetic operators

x = 15

y = 4

print(x + y) # 19

print(x - y) # 11

print(x * y) # 60

print(x / y) # 3.75

print(x % y) # 3

print(x ** y) # 50625

print(x // y) # floor division gives integer result 3
  

print("--------------------Assignment Operators--------------------")

x = 10

print("Starting value: x", x) # 10


x = 10

print("\nAfter = :", x) # 10


x += 5 

print("After += 5:", x) # x = x + 5 = 15

x -= 3

print("After -= 3:", x) # x = x - 3 =12


x *= 2

print("After *= 2:", x) # 24


x /= 4

print("After /= 4:", x) # 6


x //=2

print("After //=2:", x) # 3


x %= 3

print("After %= 3:", x) # x = x % 3 = 0


x = 6

print("\nReset x =", x) # 6


x **= 2

print("After **= 2: ", x) # x = x ** 2 = 36


print("--------------------Logical Bitwise Operators--------------------")

x = 6

print("\nReset x =", x) # 6


x &= 3

print("After &= 3: ", x) # x = x & 3 = 6 & 3 


x != 2

print("After != 2:", x) # 2


x ^= 5

print("After ^= 5:", x) # 7


x = 4

print("\nReset x =", x) #


x <<= 2

print("After <<= 2:", x) #


x = 4

x >>= 1

print("After >>= 1:", x)


print("--------------------Comparsion Operators--------------------")

x = 5

y = 3

def jls_extract_def():
    # 
    return 


print(x == y) #  

print(x != y) #

print(x < y) #

print(x >= y) #

print(x <= y) #

print("--------------------- Identiy Operators----------------------")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # trure
print(x is y) # false
print(x == y) # true

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # true
print(x is y) # false

print("-------------------Membership operators--------------------")
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # true

fruits  =["apple", "banana", "cherry"]
print("orange" not in fruits) # true

text = "Hello World"
print("H"in text) # true
print("hello" in text) # false
print("z" not in text ) # true


print("--------------------Ternary operator--------------------")
num = 10
res = "Even" if num % 2 == 0 else "Odd"
print(res) #Even

#WAP to fin larges of 3 numbers
a = 10
b = 20
c = 30
greatest = a if a > b and  a > c else b if b > c else c
print("Greatest number is:", greatest)
 

#WAP to find num is positive or negative
num = int(input("Enter the number: "))
print("Positive" if num > 3 else "Negative")
 

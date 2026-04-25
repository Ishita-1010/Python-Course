Name = input("My name is: ")
Age = input("I am: ")
Profession = input("I work as:")

print(Name, Age, Profession)

a = int(input("Enter first variable:"))
b = int(input("Enter second variable:"))

print("First Variable: a =", a, ",Second Variable: b = ", b)

a = a + b
b = a - b
a = a - b

print("First Variable: a =", a, ",Second Variable: b = ",b)

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

print(x+y, x-y, x*y, x/y)

c = float(input("Enter the temperature in Celsius:"))

f = (c * 1.8)+32

print(c)
print(f)

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = float(input("Enter the third number:"))

if (a>=b) and (a>=c):
    print("a is the greatest number")

elif (b>=c) and (b>=a):
    print("b is the greatest number")

else:
    print("c is the greatest number")



a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = float(input("Enter the third number:"))
d = float(input("Enter the fourth number:"))

if (a>b):
    largest = a
    second_largest = b
else:
    largest = b
    second_largest = a

if (c>largest):
    largest = c
    second_largest = largest
elif (c>second_largest):
    second_largest = c

if (d>largest):
    largest = d
    second_largest = largest
elif (d>second_largest):
    second_largest = d

print("The second largest number is:", second_largest)

n = float(input("Enter a number:"))

if (n % 2 == 0 ):
    print("n is an even number")

else:
    print("n is an odd number")

a = float(input("Enter a number"))

if ((a % 3 == 0) & (a % 5 == 0)):
    print("a is divisible by 3 and 5")

else:
    print("a is not divisible by 3 and 5")


tuple = (0,1,2,3,4)
tuple[1] = 6
print(tuple)

s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)

s= "My name is {} and I am {} years old".format("Ishita", 30)
print(s)

s1 = "geeksforgeeks"
s2 = "geeks"

print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2, 0, 13))

s = input("Enter a text")

s= s.lower()

a = s[::-1]

if a==s:
    print("This is palindrome")

else:
    print("This is not palindrome")

PI = 3.142
r = int(input("Enter the radius if the circle"))

area = PI * r*2

print(area)

length = int(input("Enter the length of the rectangle"))
width = int(input("Enter the width of the rectangle"))

area_rectangle = length * width

print(area_rectangle)

base = int(input("Enter the base of the triangle"))
height = int(input("Enter the height of the triangle"))

area_triangle = (base * height)/2

print(area_triangle)

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

option = input("Enter option (1/2/3/4/5): ")

if option in ['1', '2', '3', '4', '5']:
    if option == '5':
        print("Exiting the calcultor")

    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))

    if option == '1':
        result = num1 + num2
        print(num1 , "+" , num2, "=", result)
    
    elif option == '2':
        result = num1 - num2
        print(num1, "-", num2, "=", result)

    elif option == '3':
        result = num1 * num2
        print(num1, "*", num2, "=", result)

    elif option == '4':
        if num2 != 0:
            result = num1 / num2
            print(num1, "/", num2, "=", result)
        else:
            print("Error! Number cannot be divided by zero")
else:
    print("Invalid Option! Please select from the given option.")

a = [1,2,3,4,5]

a.append(6)
print("After append:(6):", a)

a.insert(1, 8)
print("After insert(1, 8):", a)

a.extend([9,10,11,12])
print("After extend([9,10,11,12]):", a)

a.clear()
print("After clear:", a)

a = [10,20,30,40,50]

popped_val = a.pop()

print(a)

def process_numbers_string(numbers_string):
    # 1. Parse the string into a list of numbers
    # Assuming numbers are space-separated for this example
    numbers_list = [int(num) for num in numbers_string.split()]

    # 2. Remove duplicates using a set
    unique_numbers_set = set(numbers_list)

    # 3. Convert back to a list and sort
    sorted_unique_numbers = sorted(list(unique_numbers_set))

    return sorted_unique_numbers

input_string = "5 2 8 1 2 5 9 3"
result = process_numbers_string(input_string)
print(result)

import random
num = random.randint(1, 70)

print(num)


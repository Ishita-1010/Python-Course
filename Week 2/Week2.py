tup = ()
print(tup)

li = [1,2,3,4,5]
print(tuple(li))

tup = tuple('Geeks')
print(tup)

tup = ('Ishita')
n = 5

for i in range(int(n)):
    tup = (tup,)
    print(tup)

tup = ("Geeks", "For", "Geeks")

a,b,c = tup

print(a,b,c)
print(a)
print(b)
print(c)

a = [1,2,3,(4,5),6,7]

c = next((i for i, x in enumerate(a) if isinstance(x,tuple)),len(a))

print(c)

from collections import namedtuple
import collections

Student = namedtuple('Student', ['name', 'age', 'DOB'])

S = Student('Ishita', '31', '10101994')

print("The student age using index is:", end="")
print(S[1])

print("The studen name using keyname is:", end="")
print(S.name)

print("The student age using getattr():", end="")
print(getattr(S, 'DOB'))

Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

S = Student('Ishita', '31', '10101994')

li = ["Sourabh", '34', '18121990']

di = {'name': "Ishani", 'age': 37, 'DOB': '25121988'}

print(Student._make(li))
print(S._asdict())
print(Student(**di))

a = (1,2,3,4,5)
b = (100,200,300,400,500)

print(f"Before Swap a is {a}, b is {b}")

a,b = b,a

print(f"After Swap a is {a}, b is {b}")

li = [5,7,4,7,4,3,5]

li.sort()

print(li)

li.sort(reverse=True)

print(li)

li = list(set(li))

print(li)

li = list(dict.fromkeys(li))

print(li)

a = [2,4,2,8,1,4,6]

res = []

[res.append(val) for val in a if val not in res]

res.sort()

print(res)

res = []

for val in a:
    if val not in res:
        res.append(val)

print(res)

string = input("Enter a string:")
 
vowel = 0
consonant = 0 

for i in string:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        vowel+=1
    elif i.isalpha():
        consonant+=1

print(string)
print("Vowels:", vowel, "Consonant:", consonant)

#Set

set1 = {1,2,3,4,5}

set1.add(6)

print(set1)

set1.update([7,8])

print(set1)

set1.remove(4)

print(set1)

set1.discard(10)

print(set1)

# Palindrome

string = input("Enter a string")

if string == string[::-1]:
    print("This is palindrome")

else:
    print("This is not palindrome")

#Character frequency

string = input("Enter a string")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(string)
print(frequency)

#replace vowel with *

string = input("Enter a string")

v = "aeiouAEIOU"
rep = "*"
replaced_string = string

for vowel in v:
    replaced_string = replaced_string.replace(vowel, rep)


print(string)
print(replaced_string)

string = input("Enter a string")

vowels = "aeiouAEIOU"

replaced_string = "".join("*" if char in vowels else char for char in string)

print(replaced_string)

#remove duplicate from list

my_list = input("Enter a list")

unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(my_list)
print(unique_list)


my_list = input("Enter numbers")

unique_list = list(dict.fromkeys(my_list))

print(unique_list)

#smallest and largest

my_list = list(map(int, input("Enter a list").split()))

smallest = min(my_list)
largest = max(my_list)

print("The smallest element is:", smallest)
print("The largest element is:", largest)

#rotate list

my_list = list(map(int, input("Enter a list").split()))

n = 3

rotated_list = my_list[-n:] + my_list[:-n]

print(my_list)
print(rotated_list)

#merge sorted list

list1 = list(map(int, input("Enter first list").split()))
list2 = list(map(int, input("Enter second list").split()))

list3 = sorted(list1 + list2)

print(list1)
print(list2)
print(list3)

import heapq

a = list(map(int, input("Enter first list").split()))
b = list(map(int, input("Enter second list").split()))

c= list(heapq.merge(a,b))

print(a)
print(b)
print(c)

import numpy as np

a = np.array(input("Enter first list").split())
b = np.array(input("Enter second list").split())

c = np.sort(np.concatenate((a,b)))

print(a)
print(b)
print(c.tolist())

#Manual Search

list_1 = list(map(int, input("Enter first list").split()))
search_item = int(input("Enter a number to search"))

found = False

for val in list_1:
    if val == search_item:
        found = True
        print(f" '{val}' found in the list")
        break

if not found:
    print(f" '{search_item}' not found in the list")

list_1 = input("Enter first list").split()
search_item = input("Enter an item to search").lower()

found = False

for item in list_1:
    if item.lower() == search_item:
        found = True
        print(f" '{item}' found in the list")
        break

if not found:
    print(f" '{search_item}' not found in the list")

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a & b < c:
    print(f" '{c}' is the greatest number")

elif b & c < a:
    print(f" '{a}' is the greatest number")
    
else:
    print(f" '{b}' is the greatest number")

# Dictionary

d1 = {1: 'Ishita', 2: 'Sourabh', 3: 'Ishani'}
print(d1)

d2 = dict(a= "Ishita", b= "Sourabh", c= "Ishani")
print(d2)

d3 = {'name':'Ishita', 1: 'Python', (1,2): [1,2,4]}

print(d3)
print(d3["name"])
print(d3.get("name"))
print(d3[1])
print(d3.get(1))
print(d3[(1,2)])
print(d3.get((1,2)))

d1 = {1: 'Ishita', 2: 'Sourabh', 3: 'Ishani'}
print(d1)

d1["age"] = 30

print(d1)

d2 = dict(a= "Ishita", b= "Sourabh", c= "Ishani")
print(d2)

d3 = {'name':'Ishita', 1: 'Python', (1,2): [1,2,4]}

d2["a"] = "Ishitaaa"

print(d2)

del d1[3]

print(d1)

val = d1.pop(2)
print(val)

key, val = d2.popitem()
print(f"Key: {key}, Value: {val}")

d3.clear()
print(d3)

d4 = {1: 'Ishita', 2: 'Sourabh',3: {'A': 'Welcome', 'B': 'To', 'C': 'Python'}}
print(d4)

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

myDict = {k:v for (k,v) in zip(keys,values)}

print(myDict)

dic = dict.fromkeys(range(6), True)

print(dic)

dic1 = {x: x**2 for x in [1,2,3,4,5]}
print(dic1)

dic2 = {x.upper(): x*3 for x in 'coding'}
print(dic2)

mydict1 = {x:x**3 for x in range(10) if x**3 % 4 == 0}
print(mydict1)

word = 'ISHITA'

d6 = {x:{y: x+y for y in word} for x in word}

print(d6)

#Lambda
n = [1,2,3,4,5,6,7,8]
even = filter(lambda x: x%2==0, n)
print(list(even))

calc = lambda x, y: (x+y, x*y)
res = calc(3,4)
print(res)

a=[1,2,3,4,5]
b= map(lambda x:x*2, a)
print(list(b))

from functools import reduce
a = [1,2,3,4,5]
b = reduce(lambda x,y: x*y, a)
print(b)

#MAP

def double(val):
    return val * 2

a = [1,2,3,4,5]
res = list(map(double, a))
print(res)

a = [1,2,3,4]
b = [5,6,7,8]

res = map(lambda x,y: x+y,a,b)
print(list(res))

fruits = ['apple','banana','cherry']
res = map(str.upper, fruits)
print(list(res))

#Dictionary Creation from list

a = ["gfg", "is", "best"]
k = "def_key_"

res = {f"{k}{ele}": ele for ele in a}
print(res)

a=["gfg", "is", "best"]
k= "def_key_"

res = dict.fromkeys(map(lambda x: k+x, a))

for ele in a:
    res[k+ele] = ele

print(res)

a=["gfg", "is", "best"]
k= "def_key_"

res={}
for ele in a:
    res[k+ele] = ele

print(res)

#Dictionary Creation from string

import ast

s = "{'A':10, 'B': 20, 'C': 30}"

res = ast.literal_eval(s)
print(res, type(res))

import json

s = "{'A':10, 'B': 20, 'C': 30}".replace("'", '"')
res = json.loads(s)

print(res, type(res))

#Dictionary from Text File

with open('input.txt', 'w') as f:
    f.write("name: Ishita\nage: 30\ncountry: India")

with open('input.txt', 'r') as file:
    res = {key.strip(): value.strip() for key, value in 
        (line.split(':', 1) for line in file)}
    
print(res)

with open('input.txt', 'w')as f:
    f.write("name: Ishita\nage: 30\ncountry: India")

with open('input.txt', 'r') as file:
    res = dict(line.strip().split(':', 1) for line in file)

print(res)

import csv
with open('input.txt', 'w')as f:
    f.write("name: Ishita\nage: 30\ncountry: India")

with open('input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=":")
    res = {row[0].strip(): row[1].strip() for row in reader if len(row)==2}

print(res)

with open('input.txt', 'w')as f:
    f.write("name: Ishita\nage: 30\ncountry: India")

with open('input.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(':', 1)
        res[key.strip()] = value.strip()

print(res)

#Create Dictionary Of Tuples

d = {("India", "USA"): 'Country',
       ("Red", "Blue", "Green"): 'Colours'}

print(d)

d = dict([
    ('Country',('USA', 'India')),
    ('Colours', ('Red', 'Blue', 'Green'))
])

print(d)

a = ['Country', 'Colours']
b = [('USA', 'India'), ('Red', 'Blue', 'Green')]

d = {name: feature for name , feature in zip(a,b)}

print(d)

from collections import defaultdict

d = defaultdict(tuple)
d['Country'] = ('USA', 'India')
d['Colours'] = ('Red', 'Blue', 'Green')

print(d)

# Create a Dictionary with Key as First Character
# and Value as Words Starting with that Character - Python

t = "Hello World"
res = defaultdict(list)

for w in t.split():
    res[w[0]].append(w)

print(dict(res))

t = "Welcome to Python"
res = {}

for w in t.split():
    res.setdefault(w[0], []).append(w)

print(res)

#Loops

# For Loop

s = "gfg"

for x in s:
    print(x)
    print(x)

for x in range(20):
    if x%6 == 0:
        print(x)

l = [10,20,30,40]

for i in range (len(l)):
    print(i, l[i])

for i in range(0, 10, 2):
    print(i)

for i in 'geeksforgeeks':
    if i=='e' or i=='s':
        continue
    print(i)

for n in range(5,10):
    print(n, end="")

l = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for num in l:
    sum+=num
print(sum)

l = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for num in l:
    if num%2 == 0:
        continue
    sum += num
        
print(sum)

a = [[1,2,3], [4,5,6],[7,8,9]]

for row in a:
    for num in row:
        if num==3:
            continue
        print(num)

i = 0

while i < 10:
    if i == 5:
        i+=1
        continue
    print(i)
    i += 1

i = 0

while i<10:
    i+=1
    if i == 5:
        continue
    print(i)

x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

for i in range(5):
    if i == 3:
        pass
    else:
        print(i)

for i in range(5):
    if i == 3:
        pass
    print(i)

#If else

age = int(input("Enter the age"))

if age <=12:
    print("Ticket is free")
else:
    print("Ticket is not free")

age = int(input("Enter the age"))

ticket = "Free" if age <= 12 else "Not free"

print(f"Status: {ticket}")

s = input("Enter a string")

uppercase_count = 0
lowercase_count = 0

for char in s:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    else:
        pass
print(f"String: {s}")
print(f"No of uppercase character: {uppercase_count}")
print(f"No of lowercase character: {lowercase_count}")

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))
d = int(input("Enter 4th number"))

if a>b:
    if a>c:
        if a>d:
            print("a is greatest")
        else:
            print("d is greatest")
else:
    if b>c:
        if b>d:
            print("b is greatest")
        else:
            print("d is greatest")
    else:
        if c>d:
            print("c is greatest")
        else:
            print("d is greatest")

# While loop

cnt = 0

while (cnt<3):
    cnt = cnt + 1
    print("Hello World")

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1

# Nested Loops

x = [1,2]
y = [4,5]

for i in x:
    for j in y:
        print(i,j)

for i in range(2,5):
    for j in range(1,11):
        print(i, "*", j, "=", i*j)
    print()

l1 = ['I am', 'You are']
l2 = ['healthy', 'fine', 'geek']

l2_size = len(l2)

for item in l1:
    print("start outer loop")
    i = 0
    while(i<l2_size):
        print(item, l2[i])
        i = i+1
    print("end loop")

for i in range(2,4):
    for j in range(1,11):
        if i==j:
            break
        print(i, "*", j, "=", i*j)
    print()

for i in range(2,4):
    for j in range(1,11):
        if i==j:
            continue
        print(i, "*", j, "=", i*j)
    print()

#Multiplication table
num = int(input("Enter the number for multiplication:"))

limit = int(input("Enter the limit for multiplication:"))

print(f"\nMultiplication table of {num}:")

for i in range(1, limit + 1):
    result = num * i
    print(f"{num} * {i} = {result}")

num = int(input("Enter the number for multiplication:"))

limit = int(input("Enter the limit for multiplication:"))

print(f"\nMultiplication table of {num}:")

for i in range(1, limit + 1):
    print(num, "*", i, "=", num*i)


# Sum of digits
num = int(input("Enter a number"))
sum1 = 0

while num > 0:
    sum1 += num % 10
    num //= 10
print(sum1)


num = input("Enter a number")
sum_digits = sum(int(digit)for digit in num)
print("Sum of digits:", sum_digits)

# Prime numbers in range

lower = int(input("Enter the lower range:"))
upper = int(input("Enter the upper range:"))

print(f"Prime numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num*0.5)+1):
            if (num % i) == 0:
                break
        else:
            print(num)

number = int(input("Enter a number:"))

if number <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(number*0.5)+1):
        if number % i == 0:
            is_prime = False
            break
    print(is_prime)



#Factorial program

num = int(input("Enter a number"))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")
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

    
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
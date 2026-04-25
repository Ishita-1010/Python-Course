# Function

def fun():
    print("Welcome to week3")

fun()

x = int(input("Enter a number"))

def evenOdd(x):
    if (x % 2 == 0):
        print("The number is Even")
    else:
        print("The number is odd")

evenOdd(x)

a = int(input("Enter a number"))
b = int(input("Enter second number"))

def sub(a,b):
    return(a-b)

res = sub(a,b)
print("Subtraction of ",a, "and", b, "is", res)

#prime number

def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5)+1):
            if x % d == 0:
                break
        else:
            print(x)
            count += 1
        x += 1

n = 10
fun(n)

user_num = int(input("Enter a number"))

def is_prime(num):
    if num < 2:
        return False
    for d in range(2, int(num ** 0.5)+1):
        if num % d == 0:
            return False
    return True

if is_prime(user_num):
    print(f"{user_num} is prime")
else:
    print(f"{user_num} is not prime")
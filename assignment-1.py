#ASSIGNMENT-1 ABHI AGRAWAL 1024170052



#Assingment 1.1: WAP to print your name three times
	
name = input("Enter your name: ")

for i in range(3):
    print(name)

#Assingment 2.1: WAP to add three numbers and print the result.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = num1 + num2 + num3

print("The sum is:", result)

#Assingment 2.2: WAP to concatinate three strings and print the result.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str3 = input("Enter third string: ")

result = str1 + str2 + str3

print("Concatenated string:", result)

#Assingment 4.1: WAP to print the table of 7, 9.

print("Table of 7:")

for i in range(1, 11):
    print(7 * i)

print("\nTable of 9:")

for i in range(1, 11):
    print(9 * i)

#Assingment 4.2: WAP to print the table of n and n is given by user.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n * i)

#Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)

#Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maximum = max(num1, num2, num3)

print("Maximum number is:", maximum)

#Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        sum = sum + i

print("Sum =", sum)

#Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.


n = int(input("Enter a number: "))

sum = 0

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        sum = sum + i

print("Sum of prime numbers =", sum)

def add_odd_numbers(n):
    sum = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            sum = sum + i
print("Sum of prime numbers =", sum)

#Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.

def add_odd_numbers(n):
    sum = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            sum = sum + i

    return sum


n = int(input("Enter a number: "))

result = add_odd_numbers(n)

print("Sum of odd numbers =", result)


#Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user.

def add_prime_numbers(n):
    sum = 0

    for i in range(2, n + 1):
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            sum = sum + i

    return sum


n = int(input("Enter a number: "))

result = add_prime_numbers(n)

print("Sum of prime numbers =", result)
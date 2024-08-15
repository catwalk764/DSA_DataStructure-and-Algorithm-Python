#!/usr/bin/env python3

# recursive method O(2^n) Expontinal
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci (n - 2)

user_input = int(input("Enter non negative number to find fibonacci :"))
print(f"{fibonacci(user_input)}")

######################################################################

'''
Iterative method O(n) Linear
def fibonacci(number):
   
    a, b = 0, 1

    for _ in range(2, number+1):
        a, b = b, a+b
    return b

try:
    user_input = int(input("Enter a non-negative integer to find its Fibonacci: "))
    print(f"The Fibonacci number is: {fibonacci(user_input)}")
except ValueError:
    print("Invalid input! Please enter a valid non-negative integer.")


'''

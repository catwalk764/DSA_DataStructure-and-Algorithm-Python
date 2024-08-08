#!/usr/bin/env python3

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci (n - 2)

user_input = int(input("Enter non negative number to find fibonacci :"))
print(f"{fibonacci(user_input)}")

######################################################################


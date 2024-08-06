#!/usr/bin/env python3

def constant_time(arr, index):
    return arr[index]

arr = [10,20,60,30,200]
print(constant_time(arr, 0))
print(constant_time(arr, 4)) #output is 10 200
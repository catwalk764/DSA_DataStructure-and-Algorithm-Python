#!/usr/bin/env python3

def liner_time(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
arr = [21, 36, 54, 1, 25, 8, 9, 3, 5, 48, 3]
print(liner_time(arr, 1))
#!/usr/bin/env python3
#The function binary is actually implementing a binary search algorithm. 
# It's designed to find the index of a target value in a sorted array.
# First code finds the index of target value, second value of give index.
'''def binary(arr, target):
    if len(arr) <= 1:
        return arr
    
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [2, 36, 9, 65, 7, 4, 78, 5, 5, 7]
arr.sort()
print(arr)
print("index of the element is :", binary(arr, 7))'''

def binary(arr, index):
    left = 0
    right = len(arr) -1

    if 0 <= index < len(arr):
        return arr[index]
    return None
arr = [2, 36, 9, 65, 7, 4, 78, 5, 5, 7]
arr.sort()
print(arr)
print("value at index is:", binary (arr, 7))
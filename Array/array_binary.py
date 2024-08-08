#!/usr/bin/env python3

def binary(arr, target):
    if len(arr) <= 1:
        return arr
    
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = len(arr) // 2
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
print("index of the element is :", binary(arr, 7))
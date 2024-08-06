#!/usr/bin/env python3

def binary_search(arr, target):
    left, right = 0, len(arr) - 1 # initializing the left and right values, let say array have 3 elements then left is 0, right is 2.

    while left <= right:
        mid = (left + right) // 2 # finding the mid value of the array.

        if arr[mid] == target:
            return mid          # target found
        elif arr[mid] < target:
            left = mid + 1       # searching in the right half
        else:
            right = mid - 1      # searching in the left half

    return -1                   # target not found

arr = [10, 25, 3, 6, 9, 45, 25, 87, 26, 1, 45, 8, 100, 36, 25, 84, 36, 1, 47, 58, 63, 25, 456, 0]
arr.sort()
print("sorted array",arr)
print(binary_search(arr, 84))

        
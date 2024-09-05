#!/usr/bin/env python3

def mergesort(arr):
    if len(arr) <= 1: # Base case: If the array has 1 or 0 elements, it's already sorted.
        return arr
    
    # Split the array into two halves
    mid = len(arr) //2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])

    # Merge the two sorted halves
    result = []

    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append (left_half[i])
            i+=1
        else:
            result.append(right_half[j])
            j+=1

    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result
arr = [1, 23, 78, 8, 6, 41]
sorted_arr = mergesort(arr)
print ("sorted array is", sorted_arr)

    


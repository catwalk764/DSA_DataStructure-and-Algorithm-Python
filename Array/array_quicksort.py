#!/usr/bin/env python3
#Divide and Conquer Pattern: using pivot, choosing pivot differs the Time and space complexity.
def quicksort(arr):
    if len(arr) <= 1: #This is the base case of the recursive function
        return arr
    
    '''
    pivot = len(arr) // 2:

This would give the index of the middle element, not the actual value.
For example, if your array is [3, 6, 8, 12, 9, 1, 5, 2], then len(arr) // 2 gives you 4, which is the index of the middle element, not the pivot value itself.
pivot = arr[len(arr) // 2]:

This gives the value at the middle index of the array.
Using the same array [3, 6, 8, 12, 9, 1, 5, 2], the index is 4, and arr[4] is 9. So, the pivot is the actual element value 9, not the index 4.
    '''
    pivot = arr[len(arr) // 2]

    '''
This line creates a new list left that contains all elements from the array arr that are less than the pivot.
The part x for x in arr is a list comprehension in Python:
x for x in arr means "for every element x in the array arr, do something with x."
The condition if x < pivot means it will only include elements x that are less than the pivot in the new list.
Effectively, it's a concise way of writing a for loop that filters out elements less than the pivot and creates a new list.
    '''
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [3, 6, 8, 12, 9, 1, 5, 2]
print(quicksort(arr))

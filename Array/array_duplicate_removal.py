#!/usr/bin/env python3
'''
Two Pointers Approach for Removing Duplicates:
The Two Pointers approach is an efficient technique used to solve problems involving sorted arrays, 
such as removing duplicates. In this method, two pointers are utilized: one to traverse the array
and the other to track the position to write unique elements.

Note: This method is specifically designed for sorted arrays. 
If you need to remove duplicates from an unsorted array, 
additional steps (such as sorting or using a hash set) would be required.

'''
def duplicate_removal(arr):
    if not arr: # Handle the edge case of an empty array
        return arr
    
    write_index = 1 # Start writing unique elements from index 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]: # Compare current element with the previous one
            arr[write_index] = arr[i]
            write_index += 1
    return write_index  # New length of the array without duplicates

arr = [1, 3, 5, 5, 1, 0]
current_arr_lenght = len(arr)
print("Current lenght of the array is: ", current_arr_lenght)
lenght = duplicate_removal(arr)
print("New length is", lenght )
print("Array after removing duplicates", arr[:lenght])
    
#!/usr/bin/env python3

def merge_sort(arr):
    if len(arr) <= 1:
        return arr # Base case: a single element array is already sorted.
    

    mid = len(arr) // 2 #it gives the middle index
    left_merge = merge_sort(arr[:mid]) #recursively sort the left half
    right_merge = merge_sort(arr[mid:])#recursively sort the right half

    return merge (left_merge, right_merge) #merge the sorted halves

def merge(left, right):
    sorted_array= []
    i=j=0

    #merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1


    #Append any remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

arr =[1, 2, 5, 56, 96, 75, 2, 3, 78, 5, 9, 7, 56, 99, 25, 47, 36]
sorted_arr = merge_sort(arr)
print(sorted_arr)






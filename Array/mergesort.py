#!/usr/bin/env python3
'''
Merge Sort:
Explanation: A divide-and-conquer algorithm. It divides the array into halves, recursively sorts each half, and merges them back together.
Time Complexity: O(n log n) in all cases (best, average, and worst).
Best for: Large datasets where efficiency is important.
Steps:
Divide the array into two halves.
Recursively sort each half.
Merge the two sorted halves back into one sorted array.

How It Works:
Initial Merging: During the merging phase, elements are compared from the left_half and right_half arrays and added to the result array until one of the halves is exhausted.

Remaining Elements:

If the left_half is not exhausted, it means all its remaining elements are greater than the elements in the right_half that have already been added to the result. These remaining elements in left_half should be added to the result.
Similarly, if the right_half is not exhausted, its remaining elements should be added to the result.
Example to Illustrate:
Let’s say we have the following two sorted halves that we want to merge:

left_half = [1, 3, 5]
right_half = [2, 4, 6]
During the merging process, we compare and add elements to result:

Compare 1 and 2: 1 is smaller, so it’s added to result. (result = [1])
Compare 3 and 2: 2 is smaller, so it’s added to result. (result = [1, 2])
Compare 3 and 4: 3 is smaller, so it’s added to result. (result = [1, 2, 3])
Compare 5 and 4: 4 is smaller, so it’s added to result. (result = [1, 2, 3, 4])
Compare 5 and 6: 5 is smaller, so it’s added to result. (result = [1, 2, 3, 4, 5])
At this point, left_half is exhausted, but right_half still has 6 left. '''

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
#Adds any remaining elements from the left half to result if the right half has been completely traversed.
#Adds any remaining elements from the right half to result if the left half has been completely traversed.
    result.extend(left_half[i:]) 
    result.extend(right_half[j:])

    return result

arr = [1, 23, 78, 8, 6, 41]
sorted_arr = mergesort(arr)
print ("sorted array is", sorted_arr)

    


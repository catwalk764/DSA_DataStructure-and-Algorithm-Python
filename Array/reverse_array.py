#!/usr/bin/env python3

def reverse_array(arr):
    if len(arr) <= 1: # checking the array is less than 1 if so return the actual array itself.
        return arr
    
    left, right = 0, len(arr) -1 # Creating two pointers left as '0' and right as len(arr) -1 which is 4.

    while left < right: # loops iterates until left is lesser than right.
        arr[left], arr[right] = arr[right], arr[left]
        left +=1 # incrementing left to increase index to the next one.
        right -=1 # decresing from right to move into next index
    return arr

arr = [1,2,3,4,5]
#result = reverse_array(arr)
print ("The Reversed array is:", reverse_array(arr))

'''
Step-by-Step Example:
Initial array: [1, 2, 3, 4, 5]

left = 0, right = 4
Swap arr[0] with arr[4]: [5, 2, 3, 4, 1]
Increment left to 1, decrement right to 3.
Second iteration:

left = 1, right = 3
Swap arr[1] with arr[3]: [5, 4, 3, 2, 1]
Increment left to 2, decrement right to 2.
At this point, left is no longer less than right (both are equal at index 2), so the loop stops.
'''
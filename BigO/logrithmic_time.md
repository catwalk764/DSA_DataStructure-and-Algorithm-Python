O(log n) - Logarithmic time:
---------------------------
Complexity when the running time decreases as the input increases. This is typically occurs in algorithms that repeatedly divide the problem size in half. 

Example: Binary Search:
-----------------------
How Binary Search Works:

1. Sorted Array: Binary search requires that the input array be sorted. If the array is not sorted, binary search will not work correctly.

2. Divide and Conquer: The algorithm divides the search interval in half repeatedly. It compares the target value to the middle element of the array:

1. If the target value is equal to the middle element, the search is complete.
2. If the target value is less than the middle element, the search continues on the left half of the array.
3. If the target value is greater than the middle element, the search continues on the right half of the array.

3. This process continues until the target value is found or the search interval is empty.

Example with sample array:
-------------------------
The given array:
[12, 25, 26, 78, 100, 25, 14, 1, 2, 6, 9, 8, 7, 2, 5, 6, 4, 8]

When sorted, it becomes:
[1, 2, 2, 4, 5, 6, 6, 7, 8, 8, 9, 12, 14, 25, 25, 26, 78, 100]

Target Value
Let's say we want to find the target value 25 in the sorted array.

Steps of Binary Search
Initialization:

Set left to 0 (the index of the first element).
Set right to 17 (the index of the last element, which is len(array) - 1).


left = 0, right = 17
First Iteration:

Calculate the middle index:
mid = 0 + 17 // 2 = 8 

Check the middle element:
array[8] = 8

Compare:
Since 8 (middle element) is less than 25 (target), update left:


left = mid + 1 = 9
Second Iteration:

Calculate the new middle index:
mid = 9 + 17 // 2 = 13

Check the middle element:
array[13] = 25

Compare:
Since 25 (middle element) is equal to 25 (target), we have found the target value!

Summary of Steps
Initial State:

Array: [1, 2, 2, 4, 5, 6, 6, 7, 8, 8, 9, 12, 14, 25, 25, 26, 78, 100]
Target: 25
Initial indices: left = 0, right = 17
Iteration 1:

Middle index: 8, Middle value: 8
Update left: 9
Iteration 2:

Middle index: 13, Middle value: 25
Target found at index 13.


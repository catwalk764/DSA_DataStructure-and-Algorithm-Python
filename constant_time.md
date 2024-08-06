O(1) - Constant Time
--------------------

Definition: An algorithm with O(1) complexity always takes the same amount of time to execute regardless of input size.

Explanation: No matter how large the array is, accessing the nth element always takes the same amount of time. 

Why is it Constant Time?
Array Indexing: Arrays are stored in contiguous memory locations. When you access an element by its index, the memory address of that element is calculated using a simple formula:
address = base address + ( index × size of element )

This calculation is done in constant time.

-----------------------------------------------------

Let's break down the calculation:
Suppose you have an array arr with the following values:

arr = [10, 20, 30, 40]
Base address = 1000 (where arr[0] is located)
Size of each element = 4 bytes (since these are integers)
To access arr[2] (which is 30):

address=1000+(2×4)=1000+8=1008
Thus, arr[2] is located at memory address 1008.

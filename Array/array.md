Array:
------

Introduction:
-------------

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. 

Basic Operations:
-----------------

1. Accessing Elements: Accessing elements in an array by index is done by Constant Time O(1).
2. Updating Elements: Updating elements in an array by index is done by Constant Time O(1).
3. Inserting Elements: Inserting an element at the end of the array is O(1), but inserting specific position requires shifting elements, making it O(n)in worst case.
4. Deleting Elements: Deleting an element at the end of the array is O(1), but deleting specific postiion requires shifting elements, making it O(n) in wors case.

Sorting Algorithm:
------------------

1. QuickSort:
-------------

    - Description:
        QuickSort algorithm is an efficient sorting algorithm that uses a divide-conquer startegy to sort elements. It works by selecting  a pivot element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    - Time Complexity: 
        Average Case O(n logn), worst case O(n^2).


2. MergeSort:
-------------

    - Description:
        MergeSort is a stable, divide-conquer algorithm that works by dividing the array into two halves, sorting each half, and then merging the sorted halves.

    - Time Complexity:
        O(n logn) in all best, worst, average case.


Searching Algorithm:
--------------------

1. Binary Search:
    
    - Description:
        Is a efficient algorithm for finding an item from a sorted list of item. It works by repeatedly dividing in half the portion of the list that could contain the item until you've narrowed down the possible locations to just one.

    -Time Complexity:
        O(log n)

O(n log n) - Linearithmic Time:
-------------------------------

Definition: An algorithm has O(n log n) time complexity when the running time grows in proportion to 
𝑛 multiplied by the logarithmic of 𝑛. This complexity is commonly seen in more efficient sorting algorithms and some divide-and-conquer algorithms.

Example: Merge Sort:
Merge sort is a classic example of an O(n log n) algorithm. It is a divide-and-conquer algorithm that splits the input array into smaller subarrays, sorts them, and then merges them back together.

How Merge Sort Works:
---------------------
    1. Divide: Split the array into two halves until each subarray contains a single element.
    2. Conquer: Recursively sort each subarray.
    3. Combine: Merge the sorted subarrays to produce a sorted array.

Detailed Steps of Merge Sort :

Initial Array
arr = [12, 25, 26, 78, 100, 25, 14, 1, 2, 6, 9, 8, 7, 2, 5, 6, 4, 8]
Step 1: Splitting

First Split:
Split into two halves:

Left:  [12, 25, 26, 78, 100, 25, 14, 1]
Right: [2, 6, 9, 8, 7, 2, 5, 6, 4, 8]

Second Split:
Split the left half further:

Left:  [12, 25, 26, 78]
Right: [100, 25, 14, 1]

Continue Splitting:
Keep splitting until each subarray contains a single element:
[12], [25], [26], [78], [100], [25], [14], [1], [2], [6], [9], [8], [7], [2], [5], [6], [4], [8]

Step 2: Merging:
First Merge:
Merge single-element subarrays into sorted pairs:
[12, 25], [26, 78], [25, 100], [1, 14], [2, 6], [8, 9], [2, 7], [5, 6], [4, 8]Second Merge:

Merge sorted pairs into sorted quadruples:
[12, 25, 26, 78], [1, 14, 25, 100], [2, 6, 8, 9], [2, 5, 6, 7], [4, 8]Continue Merging:

Merge sorted quadruples into larger sorted arrays until the entire array is merged back together:
[1, 12, 14, 25, 25, 26, 78, 100], [2, 2, 4, 5, 6, 6, 7, 8, 8, 9]

Finally, merge these two halves:
[1, 2, 2, 4, 5, 6, 6, 7, 8, 8, 9, 12, 14, 25, 25, 26, 78, 100]

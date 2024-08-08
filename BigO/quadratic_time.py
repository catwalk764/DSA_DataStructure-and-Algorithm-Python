#!/usr/bin/env python3

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                #swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [10, 25, 3, 8, 65, -1, 0]
print(bubble_sort(arr))


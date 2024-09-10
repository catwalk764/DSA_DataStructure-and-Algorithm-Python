#!/usr/bin/env python3

def sliding_wind(arr, k):
    n = len(arr)  # Get the length of the array
    if n < k: 
        return -1  # If the array has fewer elements than k, return -1
    
    window_sum = sum(arr[:k]) # Calculate the sum of the first 'k' elements
    max_sum = window_sum # Initialize max_sum with the initial window sum

    for i in range(n - k):  # Loop through the array from the start to n-k
        window_sum = window_sum -arr[i] + arr[i + k]  # Slide the window to the right
        max_sum = max(max_sum, window_sum) # Update max_sum if the new window sum is larger
    return max_sum

arr = [1, 23, 56, 8, 12, 34, 1, 58, 7, 69]
k=2
print("Maximum sum of subarray of size", k, "is", sliding_wind(arr, k))
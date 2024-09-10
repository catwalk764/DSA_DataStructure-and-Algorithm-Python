import random
import time

def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

def merge_sort(arr):
    if len(arr) <= 1: #Base case: If the array has 1 or 0 elements, it's already sorted.
        return arr
    # Split the array into two halves recursively, until each arry contain 1 element.
    mid = len(arr) //2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    #merging and sorting the array using comparsion


    result = [] # empty array to hold the result
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i+=1
        else:
            result.append(right_half[j])
            j+=1
    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result


        







def quick_sort(arr):
    # Implementation here
    pass

def binary_search(arr, target):
    # Implementation here
    pass

def reverse_array(arr):
    return arr[::-1]

def kadane_algorithm(arr):
    # Implementation here
    pass

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[n-k:] + arr[:n-k]

def time_operation(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def main():
    while True:
        print("\nArray Algorithms Tool")
        print("1. Generate random array")
        print("2. Enter custom array")
        print("3. Sort array")
        print("4. Search for element")
        print("5. Reverse array")
        print("6. Find maximum subarray sum")
        print("7. Remove duplicates")
        print("8. Rotate array")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            size = int(input("Enter array size: "))
            min_val = int(input("Enter minimum value: "))
            max_val = int(input("Enter maximum value: "))
            arr = generate_random_array(size, min_val, max_val)
            print("Generated array:", arr)
        
        elif choice == '2':
            arr = list(map(int, input("Enter array elements separated by space: ").split()))
            print("Entered array:", arr)
        
        elif choice == '3':
            if 'arr' not in locals():
                print("Please generate or enter an array first.")
                continue
            print("Original array:", arr)
            merged_arr, merge_time = time_operation(merge_sort, arr.copy())
            quick_arr, quick_time = time_operation(quick_sort, arr.copy())
            print("Merge sort result:", merged_arr)
            print("Merge sort time:", merge_time)
            print("Quick sort result:", quick_arr)
            print("Quick sort time:", quick_time)
        
        # Implement other menu options similarly
        
        elif choice == '9':
            print("Thank you for using the Array Algorithms Tool!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
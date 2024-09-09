#!/usr/bin/env python3
'''
Brute Force Approach (Current Code)
Algorithm:
For each number in the array (nums[i]), you check every other number (nums[j]) to see if their sum equals the target.
This approach involves nested loops where:
The outer loop iterates over each element in the array.
The inner loop checks every subsequent element to find a pair that sums to the target.
Time Complexity:
O(n²): Since you have two nested loops, where n is the number of elements in the array. Each loop performs a linear pass through the array.
Space Complexity:
O(1) (ignoring the output): You only store a few variables (i, j, and the result list).
Improved Approach: Hash Map (Dictionary) Approach
You can reduce the time complexity to O(n) by using a hash map (dictionary). The idea is to store the complement (i.e., target - nums[i]) of each element as you iterate through the array. If the complement already exists in the hash map, you've found the pair.

Algorithm:
Create an empty hash map (dictionary).
Loop through the array once:
For each element nums[i], check if its complement (target - nums[i]) is already in the hash map.
If the complement exists, return the indices.
If the complement doesn't exist, store nums[i] in the hash map with its index as the value.
If no pair is found after the loop, return an empty list.

Time and Space Complexity of Hash Map Approach
Time Complexity:
O(n): You only iterate through the array once. Each lookup and insertion in a dictionary is done in constant time, O(1), on average.
Space Complexity:
O(n): In the worst case, you store every element in the hash map, so the space complexity is linear with respect to the number of elements in the array.
Comparison: Brute Force vs. Hash Map
Time Complexity:
Brute Force: O(n²)
Hash Map: O(n) (significantly better for large input sizes)
Space Complexity:
Brute Force: O(1)
Hash Map: O(n) (slightly more space, but worth the trade-off for faster time complexity)


Hash Map Code:

class Solution():
    def twoSum(self, nums, target):
        map = {} # Dictionary to store number and its index
        for i, num in enumerate(nums): # With enumerate, you get both the index and the value directly.i represents the index.
num represents the value at that index.
            result = target - num
            if result in map:
                return [map[result], i]
            map[num] = i # store the current number and its index into dict.
        return [] #return empty list if no pair found.

    

'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] - target == nums:
                    return[i, j]
        return[]

nums = [2,7,11,15]
target = 9
solution = Solution()
print("index for the sum of two is:", solution.twoSum(nums, target))
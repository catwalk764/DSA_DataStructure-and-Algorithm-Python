#!/usr/bin/env python3

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for i in nums:
            lenght_of_nums = len(str(i))
            if lenght_of_nums % 2 == 0:
                count += 1
        return count
    
#solution = Solution()
nums = [ 1, 23, 569, 8585, 56]
print ("even digit of nums is", Solution.findNumbers(nums))
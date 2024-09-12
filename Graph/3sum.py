#!/usr/bin/env python3

class Solution(object):
    def threesum(self, nums):
        nums.sort()
        print(nums)

       #for index, i in enumerate(nums):
            #if nums[i] + nums [i] + nums[i] == 0:
                #print(nums.index)
            #else:
             #   print("its not triplets")
     
        result = []

        for i in range(len(nums)):           
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums)-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left -1]:
                        left +=1
                    while left < right and nums[right] == nums [right +1]:
                        right -=1
                elif s < 0:
                    left +=1
                else:
                    right -=1
        return result

                





solution_instance = Solution()
nums =[-1,0,1,2,-1,-4]
result = solution_instance.threesum(nums)
print(result)
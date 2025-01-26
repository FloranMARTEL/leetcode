#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zer = 0
        index=-1
        prod = 1
        for i,v in enumerate(nums):
            if v == 0:
                index = i
                zer +=1
            else:
                prod *= v
        
        if zer > 0:
            r = [0]*len(nums)
            if zer > 1:
                return r
            else:
                r[index] = prod
                return r
        
        res = [None]*len(nums) ##division egridienne
        for i in range(len(res)):
            res[i] = prod//nums[i]

        return res 

# @lc code=end


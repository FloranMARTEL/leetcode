#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
        
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j] == target:
    #                 return [i,j]
                
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        di = dict()

        for i in range(len(nums)):
            candidat = target-nums[i]
            if candidat in di:
                return [di[candidat],i]
            else:
                di[nums[i]] = i 



inp = [3,2,4]

s = Solution()
print(s.twoSum(inp,6))
        
# @lc code=end


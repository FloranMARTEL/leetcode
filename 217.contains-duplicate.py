#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# @lc code=start
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        di = Counter(nums)
        for k in di:
            if di[k] > 1:
                return True
        
        return False
        
# @lc code=end


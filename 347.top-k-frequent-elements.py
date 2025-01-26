#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from collections import Counter
# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        c = Counter(nums)
        limax = []
        for key in c:

            find = False
            pos = -1
            for index,val in enumerate(limax):
                if c[val] < c[key]:
                    find = True
                    pos = index
                    break
            
            if find == False and len(limax) < k:
                find = True
                pos = len(limax)


            if find:
                limax.insert(pos,key)

                if len(limax) > k:
                    limax.pop()
        
        return limax         


        
# @lc code=end


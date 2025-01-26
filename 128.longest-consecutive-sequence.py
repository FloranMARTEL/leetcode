#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        setnum = set(nums)

        def makedown(val):
            numshow.add(val)
            if val-1 in setnum:
                return makedown(val-1)
            else:
                return val

        def maketop(val):
            numshow.add(val)
            if val+1 in setnum:
                return maketop(val+1)
            else:
                return val

        numshow = set()
        mymax = 0
        for a in setnum:

            if a in numshow:
                continue
            
            vmax = maketop(a)
            vmin = makedown(a)

            l = (vmax-vmin)+1

            if l > mymax:
                mymax = l
        
        return mymax

# @lc code=end


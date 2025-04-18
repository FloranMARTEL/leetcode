#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        v = 0
        if x < 0:
            v=  int("-"+(str(x)[1:][::-1]))
        else:
            v= int(str(x)[::-1])


        tr1 = 2**31

        if v < tr1-1 and v > -tr1:
            return v
        
        return 0
        
# @lc code=end


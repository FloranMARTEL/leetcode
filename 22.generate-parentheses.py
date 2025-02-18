#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def rec(n,nbopen):

            if n == 0:
                return [""]

            list_possible = []

            if nbopen > 0:
                for p in rec(n-1,nbopen-1):
                    list_possible.append(")"+p)
            
            if nbopen < n:
                for p in rec(n-1,nbopen+1):
                    list_possible.append("("+p)
            
            return list_possible
        
        return rec(n*2,0)

        
# @lc code=end


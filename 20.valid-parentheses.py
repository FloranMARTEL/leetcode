#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        carracter = {
            "(":")",
            "[":"]",
            "{":"}",
        }

        pile = []
        for c in s:
            if c in carracter:
                pile.append(c)
            else:
                if len(pile) == 0:
                    return False
                
                last_open = pile.pop()
                if carracter[last_open] != c:
                    return False
        
        return len(pile) == 0
        
# @lc code=end


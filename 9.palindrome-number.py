#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)

        i = 0
        j = len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            
            i+=1
            j-=1

        return True
        
# @lc code=end


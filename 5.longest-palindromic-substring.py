#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#



# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkpalindrom(i,j,s):
            while i<j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1    
            return True
        
        maxpalin = None
        for i in range(len(s)-1):
            for j in range(len(s)-1,i,-1):
                if checkpalindrom(i,j,s):
                    candidat = s[i:j+1]
                    if maxpalin == None or len(maxpalin) < len(s[i:j+1]):
                        maxpalin = candidat
                    break
        
        if maxpalin == None:
            return s[0]

        return maxpalin

# ip = "ccc"
# s = Solution()
# print(s.longestPalindrome(ip))    
# @lc code=end


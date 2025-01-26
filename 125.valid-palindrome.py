#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import re
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)


        i = 0
        mid = len(s)//2
        while i < mid:
            if s[i] != s[len(s)-1-i]:
                return False

            i+=1
        
        return True

ip = "0P"
s = Solution()
print(s.isPalindrome(ip))
# @lc code=end


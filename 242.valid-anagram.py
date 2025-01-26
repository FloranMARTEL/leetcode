#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        conteurS = Counter(s)
        conteurT = Counter(t)
           
        
        return conteurT == conteurS
            

        
        
# @lc code=end


#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ltoi = dict()

        maxlen = None

        i = 0
        while i < len(s):

            if s[i] not in ltoi:
                ltoi[s[i]] = i
            else:
                candidat = len(ltoi)
                if maxlen == None or maxlen < candidat:
                    maxlen = candidat

                i = ltoi[s[i]]
                ltoi = dict()

            i+=1

        
        candidat = len(ltoi)
        if maxlen == None or maxlen < candidat:
            maxlen = len(ltoi)
    
        return maxlen



        
# @lc code=end


#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i1 = len(s)-1
        ip = len(p)-1

        hidec = (None,None)
        while ip>-1:

            if p[ip] == ".":
                i1-=1
            elif p[ip] == "*":
                comp = p[ip-1]
                
                if comp == ".":
                    if ip-2 > -1:
                        while s[i1] != p[ip-2]:
                            i1 -= 1
                    else:
                        return True
                
                else:
                    while i1 > -1 and s[i1] == p[ip-1]:
                        i1 -= 1

                ip -=1
                
            else:
                if s[i1] == hidec[0] and hidec[1] > 0:
                    hidec[1] -= 1
                    pass
                elif s[i1] != p[ip]:
                    return False
                else:
                    hidec = (None,None)
                i1 -=1  

            ip -=1      

        return i1 == -1


a ="aab"
b = "c*a*b"
s = Solution()
print(s.isMatch(a,b))

# @lc code=end


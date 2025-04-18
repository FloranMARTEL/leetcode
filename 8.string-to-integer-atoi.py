#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:


        num = ""

        furstdigit = True

        for i in range(len(s)):

            if s[i].isnumeric():
                num+=s[i]
            elif furstdigit and s[i] == " ":
                continue
            elif furstdigit and s[i] in {"-","+"}:
                num+=s[i]
            else:
                break
            furstdigit = False

        if len(num) == 0:
            return 0
        
        try:
            v = int(num)
        except:
            return 0
        tr1 = 2**31

        if v > tr1-1 :
            return tr1-1

        if v < -tr1:
            return -tr1
        
        return v
        

ip = "   -042"
s =Solution()
print(s.myAtoi(ip))

        
# @lc code=end


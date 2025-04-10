#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#
import string


# @lc code=start
class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:

        convDict = {}
        for i,c in enumerate(string.ascii_lowercase):
            convDict[c] = widths[i]
        
        nbligne = 0
        ligne = 0
        for c in s:

            if ligne+convDict[c] <= 100:
                ligne += convDict[c]
            else:
                ligne = convDict[c]
                nbligne += 1
        
        if ligne != 0:
            nbligne += 1

        return [nbligne,ligne]
        

ip1 = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
ip2 = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
print(string.ascii_lowercase)
s = Solution()
print(s.numberOfLines(ip1,ip2))

        
# @lc code=end


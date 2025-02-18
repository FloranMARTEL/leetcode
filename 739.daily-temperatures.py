#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:


        g = {len(temperatures)-1 : None}

        res = [0]

        for i in range(len(temperatures)-2,-1,-1):

            curent = i+1
            while curent != None:
                if temperatures[i] < temperatures[curent]:
                    res.append(curent-i)
                    g[i] = curent
                    break
                    
                curent = g[curent]
            
            if curent == None:
                res.append(0)
                g[i] = None
    
        res.reverse()

        return res


"""
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        resutl = []
        for i in range(len(temperatures)):
            find = False
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    find = True
                    resutl.append(j-i)
                    break
            
            if not find:
                resutl.append(0)


        return resutl
"""

ip = [73,74,75,71,69,72,76,73]
s = Solution()
print(s.dailyTemperatures(ip))
        
# @lc code=end


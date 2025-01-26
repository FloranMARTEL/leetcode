#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import Counter 
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        listAna : dict[str,list[str]] = dict()
        for mots in strs:
            
            cpt = Counter(mots)

            l = list(cpt.keys())
            l.sort()
            t = ""
            for v in l:
                t+= v+str(cpt[v])
            
            print(t)

            if t in listAna:
                listAna[t].append(mots)
            else:
                listAna[t] = [mots]
            
        return list(listAna.values())
            


# @lc code=end


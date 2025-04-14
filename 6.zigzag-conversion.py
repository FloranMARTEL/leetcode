#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s


        val = dict()

        lsecC = numRows*2-2

        incr = 1

        l=0

        
        for i,v in enumerate(s):

                
            sec = i//lsecC
            irel = i%lsecC

            c = (sec*(numRows-1))+((irel//(numRows-1)) * (irel%(numRows-1)))
            
            val[(l,c)]=v
            

            if l == numRows-1:
                incr = -1
            elif l == 0:
                incr = 1

            l = incr + l
            
            
        
        res = ""
        for l in range(0,numRows):
            for c in range(0,c+1):
                point = (l,c)
                if point in val:
                    res+=val[point]

        return res

        
# @lc code=end


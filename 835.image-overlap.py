#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        


        n = len(img2)

        projR1 = [None]*n
        for i in range(n):
            cpt = 0
            for j in range(n):
                cpt+= img1[i][j]
            projR1[i] = cpt

        projR2 = [None]*n
        for i in range(n):
            cpt = 0
            for j in range(n):
                cpt+= img2[i][j]
            projR2[i] = cpt

        ##

        projC1 = [None]*n
        for i in range(n):
            cpt = 0
            for j in range(n):
                cpt+= img1[j][i]
            projC1[i] = cpt

        projC2 = [None]*n
        for i in range(n):
            cpt = 0
            for j in range(n):
                cpt+= img2[j][i]
            projC2[i] = cpt

        # print(projR1)
        # print(projC1)
        # print(projR2)
        # print(projC1)

        maxprojR2 = max(projR2)
        maxprojR1 = max(projR1)

        idR2=projR2.index(maxprojR2)
        idR1=projR1.index(maxprojR1)

        t_vertical = idR2-idR1


        maxprojC2 = max(projC2)
        maxprojC1 = max(projC1)

        idC2=projC2.index(maxprojC2)
        idC1=projC1.index(maxprojC1)

        t_horizontal = idC2-idC1

        cptfin = 0
        for i in range(n):
            for j in range(n):

                if img1[i][j] ==1 and i+t_vertical < n and j+t_horizontal < n:
                    if img1[i][j] == img2[i+t_vertical][j+t_horizontal]:
                        cptfin+=1

        
        return cptfin
    
ip1 = [[1,0],[0,0]]
ip2 = [[0,1],[1,0]]

s = Solution()
print(s.largestOverlap(ip1,ip2))

        
# @lc code=end


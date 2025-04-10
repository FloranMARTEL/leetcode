#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        cptdict = dict()
        for v in nums:
            if v in cptdict:
                cptdict[v] += 1
            else:
                cptdict[v] = 1
        
        max = None

        candidat = []
        
        for v in cptdict:
            if max == None or max < cptdict[v]:
                max = cptdict[v]
                candidat = [v]
            elif max == cptdict[v]:
                candidat.append(v)
            
        # print(cptdict)
        # print(cptdict)
        minres = None
        for maxit in candidat:

            start =None
            end = None

            for i in range(len(nums)):
                if nums[i] == maxit:
                    start = i
                    break
            
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == maxit:
                    end = i
                    break

            res = (end-start)+1
            if minres == None or minres > res:
                minres = res
            

        return minres

# ip = [1,2,2,1,2,1,1,1,1,2,2,2]
# s = Solution()
# print(s.findShortestSubArray(ip))
        
# @lc code=end


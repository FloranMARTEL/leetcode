#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:


        i = 0
        j = len(height)-1
        maxW = 0

        while i < j:

            water = min(height[i],height[j]) * (j-i)

            if water > maxW:
                maxW = water
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1


        return maxW


# ip = [1,8,6,2,5,4,8,3,7]
# s = Solution()
# print(s.maxArea(ip))
# @lc code=end


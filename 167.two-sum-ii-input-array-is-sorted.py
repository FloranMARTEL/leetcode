#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:


        def find(val,n,m):

            mid = (n+m)//2

            if numbers[mid] == val and mid != i:
                return mid
            elif n == m:
                return None
            elif numbers[mid] > val:
                return find(val,n,mid)
            else:
                return find(val,mid+1,m)


        ss = set(numbers)
        for i in range(len(numbers)-1):

            tofind = target-numbers[i]
            if tofind in ss:

                j = find(tofind,0,len(numbers)-1)
                if j != None:
                    return [i+1,j+1]



i1 = [2,3,4]
i2 = 6
s = Solution()
print(s.twoSum(i1,i2))
        
# @lc code=end


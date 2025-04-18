#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        s = 0
        if root.left is not None:

            if root.left.left is None and root.left.right is None:
                s += root.left.val
            
            s += self.sumOfLeftLeaves(root.left)
        
        if root.right is not None:

            s += self.sumOfLeftLeaves(root.right)
        
        return s
            


        
        
# @lc code=end


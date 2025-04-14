#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1 = l1
        c2 = l2

        l3 = None
        c3 = None

        retenu = 0
        while c1 != None or c2 != None or retenu != 0 :
            v1 = 0
            if c1 != None:      
                v1 = c1.val

            v2 = 0
            if c2 != None:      
                v2 = c2.val

            cal = v1 + v2 + retenu
            retenu = cal//10

            if l3 == None:
                l3 = ListNode(cal%10)
                c3 = l3
            else:
                c3.next = ListNode(cal%10)
                c3 = c3.next

            
            if c1 != None:      
                c1 = c1.next

            if c2 != None:      
                c2 = c2.next

        return l3


# @lc code=end


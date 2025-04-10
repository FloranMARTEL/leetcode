#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        print(head)
        
        oldNode : ListNode= None
        curentNode :ListNode = head

        while curentNode != None:

            if curentNode.val == val:

                if oldNode == None:
                    head = curentNode.next
                else:
                    oldNode.next = curentNode.next
                    
            else:
                oldNode = curentNode
            
            curentNode = curentNode.next

                

        return head
    
ip = ListNode(val= 7, next= ListNode(val= 7, next= ListNode(val= 7, next= ListNode(val= 7, next= None))))
s = Solution()
print(s.removeElements(ip,7))
        
# @lc code=end


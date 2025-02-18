#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.pile = []
        

    def push(self, val: int) -> None:
        self.pile.append(val)
        

    def pop(self) -> None:
        self.pile.pop()
        

    def top(self) -> int:
        return self.pile[-1]
        

    def getMin(self) -> int:
        return min(self.pile)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


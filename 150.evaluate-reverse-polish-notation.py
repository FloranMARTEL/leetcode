#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        number = []


        for c in tokens:
            if c.isnumeric() or (c[0]=="-" and c[1:].isnumeric()) :
                number.append(int(c))
            else:
                op1 = number.pop()
                op2 = number.pop()
                
                match c:    
                    case "+":
                        number.append(op1+op2)
                    case "-":
                        number.append(op2-op1)
                    case "*":
                        number.append(op1*op2)
                    case "/":
                        resdiv = op2//op1
                        if resdiv < 0 and op2%op1 != 0:
                            resdiv += 1
                        number.append(resdiv)
        
        return number[0]
                        

ip = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ip = ["4","-2","/","2","-3","-","-"]
s = Solution()
print(s.evalRPN(ip))
# @lc code=end


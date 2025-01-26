#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        setcol : list[set[str]]= []
        setsubBox : list[set[str]]= []
        for i in range(9):
            setcol.append(set())
            setsubBox.append(set())

        for r in range(len(board)):
            setli = set()
            for c in range(len(board)):
                val = board[r][c]

                if val == ".":
                    continue

                elif val not in ("1","2","3","4","5","6","7","8","9"):
                    return False

                if val in setli:
                    return False
                else:
                    setli.add(val)

                if val in setcol[c]:
                    return False
                else:
                    setcol[c].add(val)
                
                
                if val in setsubBox[(r//3)*3+(c//3)]:
                    return False
                else:
                    setsubBox[(r//3)*3+(c//3)].add(val)
        
        return True
        
# @lc code=end


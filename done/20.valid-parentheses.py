#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:

    def isValid(self, s: str) -> bool:
        parStack = []
        openPar = "([{"
        closedPar =")]}"

        for char in s:
            #For when the stack is empty
            if not parStack:
                if char in closedPar:
                    return False
                else:
                    parStack.append(char)
            #For when the current character and the top of the parstack is open
            elif char in openPar and parStack[-1] in openPar:
                parStack.append(char)

            elif char in closedPar:
                if openPar.index(parStack.pop()) != closedPar.index(char):
                    return False 
        return not parStack 
        
# @lc code=end


#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ("IVXLCDM")
        runningSum = 0
        lastCharValue = 1001
        for char in s:
            idx = symbols.index(char)
            if idx % 2 == 0:
                charValue = 1*(10**(idx//2))
            else:
                charValue = 5*(10**(idx//2))
            
            if charValue > lastCharValue:
                runningSum -= lastCharValue * 2
            runningSum += charValue
            lastCharValue = charValue

        return runningSum
        
# @lc code=end


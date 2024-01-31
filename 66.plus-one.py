#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        else:
            for idx in range(len(digits)-1,0,-1):
                digits[idx] = 0
                if idx == 0:
                    digits.insert(0,1)
                else:
                    digits[idx-1] += 1

        return digits
            



# @lc code=end


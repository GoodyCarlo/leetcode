#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        len = 1
        prevInt = nums[0]
        for number in nums:
            if number != prevInt:
                nums[len] = number
                prevInt = number
                len += 1

        return len
# @lc code=end


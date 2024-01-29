#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        insert = 0
        flag = True
        for index, num in enumerate(nums):
            print(index,num)
            if num == target:
                return index
            if num >= target and flag:
                insert = index
                flag = False
    
        return len(nums) if flag else insert
        
# @lc code=end
    
test = Solution()
print(test.searchInsert([1,3,5,6],0))



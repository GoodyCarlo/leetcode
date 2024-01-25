#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        run = True
        count = 1
        prefix = ""

        while run:

            tempPrefix = strs[0][:count]
            if len(strs[0]) == count-1:
                return prefix
            for str in strs:
                if str[:count] != tempPrefix:
                    run = False
                    break
            if run:
                prefix = tempPrefix
                count += 1
        
        return prefix
           
# @lc code=end
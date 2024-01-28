#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # count = 0
        # idx = 0
        # for index, char in enumerate(haystack):
        #     if char == needle[count]:
        #         if count == 0:
        #             idx = index
        #         count += 1
        #     else:
        #         count = 0
        #         if char == needle[count]:
        #             idx = index
        #             count += 1

        #     if count == len(needle):
        #         return idx
        #     # print(char)
        #     print(count)
        # return -1
        needleLen = len(needle)
        for idx in range(len(haystack)-needleLen+1):
            if haystack[idx:idx+needleLen] == needle:
                return idx
        return -1
# @lc code=end

test = Solution()
print(test.strStr("a","a"))
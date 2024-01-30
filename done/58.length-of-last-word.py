#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        for char in s.strip():
            if char == " ":
                word = ""
            else:
                word += char
            # print(word)
        return len(word)
# @lc code=end


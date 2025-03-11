# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count the length of the last word
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        
        return count

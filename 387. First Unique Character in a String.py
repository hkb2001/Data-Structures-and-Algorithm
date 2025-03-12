# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             count = 0
#             for j in range(len(s)):
#                 if(s[i] == s[j]):
#                     count +=1
#             if(count == 1):
#                 return i
#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        #check freq
        for char in s:
            freq[char] = freq.get(char,0) + 1
        #first unique character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1
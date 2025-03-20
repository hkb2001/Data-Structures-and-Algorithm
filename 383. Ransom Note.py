# https://leetcode.com/problems/ransom-note/description/
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for char in ransomNote:
#             index = magazine.find(char)  # Find the character in magazine
#             if index == -1:
#                 return False  # Character not found, return False
#             magazine = magazine[:index] + magazine[index+1:]  # Remove the used character
#         return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}  
        for char in magazine:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        # Step 2: Check if ransomNote can be constructed
        for char in ransomNote:
            if char not in dict or dict[char] == 0:
                return False  
            dict[char] -= 1  

        return True  



# https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0  # Edge case
        return 1 + (num - 1) % 9

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0  
        return 9 if num %9 ==0 else num%9


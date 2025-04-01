# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  # Negative or ends with 0 (but not 0 itself)

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10  # Reverse last digit
            x //= 10  # Remove last digit
        
        return x == reversed_half or x == reversed_half // 10  # Compare halves

# https://leetcode.com/problems/strictly-palindromic-number/description/
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False

# Solution 2

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(n,b):
            s=""
            while n:
                s+=str(n%b)
                n//=b
            return s
        for b in range(2, n-1):
            s = convert(n,b)
            if s!=s[::-1]:
                return False
        return True
        
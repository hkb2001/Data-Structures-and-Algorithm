# https://leetcode.com/problems/student-attendance-record-i/description/

class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        for i in range(len(s)):
            if(s[i] == "A"):
                absents+=1
            if(s[i:i+3] == "LLL"):
                return False
        
        if absents >= 2:
            return False
        return True
        
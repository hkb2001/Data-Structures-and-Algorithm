# https://leetcode.com/problems/richest-customer-wealth/

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for wealth in accounts:
            current = sum(wealth)
            highest = max(highest, current)
        return highest
        
        
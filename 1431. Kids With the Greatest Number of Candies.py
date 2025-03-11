# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highCandy = max(candies)
        arr = []
        for i in candies:
            arr.append(i + extraCandies >= highCandy)
        return arr
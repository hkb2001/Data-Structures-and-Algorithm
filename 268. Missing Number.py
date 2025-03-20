# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = True
        for i in range(len(nums) + 1):
            if i not in dict:
                return i
        return -1

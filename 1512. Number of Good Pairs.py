# https://leetcode.com/problems/number-of-good-pairs/description/
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         i =0
#         j = i+1
#         count = 0
#         for i in range(len(nums)-1):
#             for j in range(len(nums)):
#                 if i < j:
#                     if nums[i] == nums[j]:
#                         count += 1
#         return count

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}  # Dictionary to store frequency of numbers
        count = 0

        for num in nums:
            if num in freq:
                count += freq[num]  # Each occurrence forms `freq[num]` good pairs
                freq[num] += 1  # Update frequency
            else:
                freq[num] = 1  # First occurrence

        return count

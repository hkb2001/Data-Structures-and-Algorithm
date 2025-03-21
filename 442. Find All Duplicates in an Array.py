# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            if num in freq:
                result.append(num)
            else:
                freq[num] = 1
        return result

        
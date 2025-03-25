# https://leetcode.com/problems/intersection-of-two-arrays/description/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for num in nums1:
            if num  in nums2 and num not in arr:
                arr.append(num)
        return arr

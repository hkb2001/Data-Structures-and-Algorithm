# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []  
        
        for num in nums:
            if num not in arr: 
                arr.append(num)
        
        for i in range(len(arr)):  # Copy back to nums
            nums[i] = arr[i]
        
        return len(arr)
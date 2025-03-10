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
    


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0  
        for j in range(1, len(nums)):  # Fast pointer
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1  # Move slow pointer
                nums[i] = nums[j]  # Update array in-place
        
        return i + 1  # Length of unique elements

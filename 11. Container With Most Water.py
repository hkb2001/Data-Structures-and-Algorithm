# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Two pointers
        max_area = 0
        
        while left < right:
            # Calculate current area
            min_height = min(height[left], height[right])
            width = right - left
            area = min_height * width
            
            # Update max area
            max_area = max(max_area, area)
            
            # Move the pointer that has the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

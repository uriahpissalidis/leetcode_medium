class Solution:
    
    def maxArea(self, h: List[int]) -> int:
        left, right = 0, len(h)-1
        area = 0
        while left < right:
            heights = min( h[left], h[right] )
            area = max( area, (right-left) * heights)
            while h[left] <= heights and left < right:
                left += 1
            while h[right] <= heights and left < right:
                right -= 1
        return area
    
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

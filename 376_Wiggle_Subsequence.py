class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        up, down = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                up = down + 1
            elif nums[i] - nums[i-1] < 0:
                down = up + 1
        return max(down, up)
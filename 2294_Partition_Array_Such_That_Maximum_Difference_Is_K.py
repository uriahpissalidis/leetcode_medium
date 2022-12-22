class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans, j = 1, 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] - nums[j] > k:
                ans += 1
                j = i
        return ans

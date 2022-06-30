class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # average won't work here because of convergence
        # edge case wherein nums is empty
        if not nums: return 0
        # sort then get the middle element
        nums.sort()
        median = self.getMedian(nums)
        ans = 0
        for num in nums:
            ans += abs(num - median)
        return ans
    
    def getMedian(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return int((nums[n//2] + nums[n//2-1]) // 2)
        else:
            return nums[n//2]
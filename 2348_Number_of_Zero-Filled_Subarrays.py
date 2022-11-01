class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = curr = 0
        for num in nums:
            if num == 0:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums) -1
        while left < right:
            sum1 = nums[left] + nums[right]
            if sum1 == k:
                count += 1
                left += 1
                right -= 1
            elif sum1 < k:
                left += 1
            else :
                right -= 1
        return count
        
        """
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b # Explain: a + b = k  =>  a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans
        """
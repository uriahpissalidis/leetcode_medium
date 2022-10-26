from math import gcd

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        # [1] we try checking every subarray
        for i in range(0, len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = gcd(g,nums[j])
                if g == k: 
                    count += 1
                if g < k: #[2] occasionally, many of them fail 
                    break
            
        return count
            
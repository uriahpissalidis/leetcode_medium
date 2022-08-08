class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
#         dp = [1] * len(nums)
        
#         for i in range(1,len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j]+1)
#         return max(dp)

        sub = [nums[0]]
        for num in nums[1:]:
            if sub[-1] < num:
                sub.append(num)
            else:
                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num
        return len(sub)
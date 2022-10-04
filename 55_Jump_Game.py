class Solution:
    def canJump(self, nums: List[int]) -> bool: # front-to-back solution
        maxAttained = 0
        for i in range(len(nums)):
            if i > maxAttained: # if you've reached somewhere that can't be traversed to
                return False
            maxAttained = max(maxAttained, nums[i] + i)
        return True
    
    def canJump(self, nums): # back-to-front solution
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
    
    # from: https://leetcode.com/problems/jump-game/discuss/2511491/Easy-to-understand-O(n)-time-Python-Solution
    def canJump(self, nums: list) -> bool: 
        count, carry = 1, nums[0]
        while carry and count < len(nums):
            carry -= 1
            carry = max(carry, nums[count])
            count += 1
        return count == len(nums)
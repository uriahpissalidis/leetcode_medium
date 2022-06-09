class Solution(object):
    def twoSum(self, nums, target):
        l = 0
        r = len(num) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
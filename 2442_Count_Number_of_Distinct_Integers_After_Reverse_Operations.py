class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = nums*2
        j = len(nums)//2
        for i in range(0, len(nums)//2):
            nums[j] = int(str(nums[i])[::-1])
            j += 1
        count = set(nums)
        return (len(count))
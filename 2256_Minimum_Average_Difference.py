class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        n = len(nums)    
        minimum = inf
        output = 0
        for i in range(len(nums) - 1):
            a = prefix[i]
            b = prefix[-1] - a
            avg1 = a // (i + 1)
            avg2 = b // (n - 1 - i)
            diff = abs(avg1 - avg2)
            if diff < minimum:
                minimum = diff
                output = i

        if prefix[-1] // n < minimum: output = n - 1
        return output

#985_Sum_of_Even_Numbers_After_Queries
#TLE brute force solution
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, count = [], 0
        for row in queries:
            index = row[1]
            value = row[0]
            nums[index] = nums[index] + value
            tempSum = 0
            for i in range(0, len(nums)):
                if nums[i] % 2 == 0:
                    tempSum = tempSum + nums[i]
            ans.append(tempSum)
        return ans
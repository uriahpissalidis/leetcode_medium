class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowLen, colLen = len(grid), len(grid[0])
        def count(nums):
            return 2*sum(nums)-len(nums)
        rows = list(map(count, grid))
        cols = list(map(count, zip(*grid)))
        
        for i,j in product(range(rowLen), range(colLen)):
            grid[i][j] = rows[i] + cols[j]
        
        return grid
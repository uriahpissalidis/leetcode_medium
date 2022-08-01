import math
class Solution:
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        return math.factorial(m+n-2)//(math.factorial(n-1) * math.factorial(m-1))
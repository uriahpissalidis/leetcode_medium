
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        # fastest solution yet
        ans, stack = [0]*len(t), []
        stack = []
        for i,cur in enumerate(t):
            while stack and cur > t[stack[-1]]:
                last = stack.pop()
                ans[last] = i-last
            stack.append(i)
        return ans
        
        # consider: utilization of a monotonic stack (decreasing) to memoize as we traverse
        # to understand the #footerComment, reference the video at link below
        # https://www.youtube.com/watch?v=cTBiBSnjO3c go to 6:50
        ans, stack = [0]*len(t), []
        for i, v in enumerate(t):
            while stack and v > stack[-1][1]: #is temp greater than the top of the stack?
                topI, topV = stack.pop()
                ans[topI] = i - topI
            stack.append((i, v))
        return ans

        # TLE solution
        n, right_max = len(temperatures), float('-inf')
        res = [0] * n
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            if right_max <= t:
                right_max = t
            else:
                days = 1
                while temperatures[i+days] <= t:
                    days += res[i+days]
                res[i] = days
        return res

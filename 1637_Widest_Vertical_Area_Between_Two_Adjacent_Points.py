class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # basically just find the max distance of your x coordinates
        l = []
        for i in points:
            l.append(i[0])
        l.sort()
        maxD = 0
        for i in range(1,len(l)):
            maxD = max(maxD, l[i]-l[i-1])
        return maxD
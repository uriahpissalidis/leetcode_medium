class Solution:
    def countCollisions(self, a: str) -> int:
        n, noCrash = len(a), 0
        if n == 1: return 0
        for i in range(0, n):
            if a[i] != 'L':
                break
            noCrash += 1
        for i in range(n-1, 0, -1):
            if a[i] != 'R':
                break
            noCrash += 1
        for i in range(0, n):
            if a[i] == 'S':
                noCrash += 1
        return n-noCrash
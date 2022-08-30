class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        # in-place solution
        A.reverse()
        n = len(A)
        for i in range(1,n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A
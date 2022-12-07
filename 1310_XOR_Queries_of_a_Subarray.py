class Solution:
    def xorQueries(self, arr: List[int], q: List[List[int]]) -> List[int]:
        ans = [0]
        for i in range(len(arr)):
            ans.append(ans[-1]^arr[i])
        res = []
        for l,r in q:
            res.append(ans[r+1]^ans[l])
        return res

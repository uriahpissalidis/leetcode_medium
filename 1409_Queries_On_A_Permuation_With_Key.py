
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        perms = [x for x in range(1, m + 1)]
        for num in queries:
            ans.append(perms.index(num))
            perms.remove(num)
            perms.insert(0,num)
        return ans

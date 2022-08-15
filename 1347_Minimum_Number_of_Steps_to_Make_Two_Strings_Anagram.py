class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # turn t into an anagram of s
        sCount, tCount, ans = Counter(s), Counter(t), len(t)
        for c in list(sCount.keys()):
            if c in tCount:
                ans = ans - min(sCount[c],tCount[c])
        return ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            letterCount = [0 for _ in range(26)]
            for word in strs[i]:
                val = ord(word)-97
                letterCount[val] += 1
            letterCount = tuple(letterCount)
            d[letterCount].append(strs[i])
        return d.values()
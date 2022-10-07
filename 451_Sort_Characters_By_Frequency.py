from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = len(s)
        d, ans = Counter(s), ''
        while count != 0: # stops when Counter's values all equal 0
            for char in d: # iterate the counter
                if d[char] == count: # ensures we pop greatest quantity first
                    ans += char * count
                    d[char] = 0
            count -= 1
        return ans
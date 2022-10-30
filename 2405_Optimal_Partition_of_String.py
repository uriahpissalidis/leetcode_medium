class Solution:
    def partitionString(self, s: str) -> int:
        # iterate through the string
        # if dupes are found, inc ans and clear set d
        # TC: O(N) || SC: O(N)
        
        d, ans = set(), 1
        for char in s:
            if char not in d:
                d.add(char)
            else:
                ans += 1
                d = set()
                d.add(char)
        return ans
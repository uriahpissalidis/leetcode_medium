class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        x = len(part)
        while part in s:
            i = s.index(part)
            s = s[:i] + s[i + x:]
        return s
        """
        # 2nd Solution
        while part in s:
            s=s.replace(part, "", 1)
        return s
        """
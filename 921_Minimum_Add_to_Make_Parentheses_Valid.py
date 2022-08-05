class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, i = [], 0
        for i in range(len(s)):
            if s[i]==')':
                if l and l[-1]=='(':
                    l.pop()
                else:
                    l.append(s[i])
            elif s[i]=='(':
                l.append(s[i])
        return len(l)
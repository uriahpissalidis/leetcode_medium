class Solution:
    def countVowelStrings(self, n: int) -> int:
        # combinations formula below
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24;
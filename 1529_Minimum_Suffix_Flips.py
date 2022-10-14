class Solution:
    def minFlips(self, target: str) -> int:
        # solution 1, cleans unnecessary 0's from the target
        # TC: O(N) || SC: O(1)
        target = target.lstrip("0")
        count = 0
        state = "0"
        for i in target:
            if i != state:
                count += 1
                state = i
        return count
    
        # solution two, utilizing XOR
        # TC: O(N) || SC: O(1)
        flip, ans = 0, 0
        for c in target:
            if int(c) ^ flip:
                ans += 1
                flip ^= 1
        return ans
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Runtime: nlogn due to sort
        # Space complexity: O(1)
        sortedPiles = sorted(piles, reverse=True)
        picks = len(piles)//3
        i, res = 1, 0
        while picks:
            res += sortedPiles[i]
            picks -= 1
            i += 2
        return res
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('Inf')]*(amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            temp = [float('Inf')]
            for c in coins:
                if i-c<0:
                    break
                temp.append(dp[i-c])
            dp[i] = min(temp)+1

        return dp[amount] if dp[amount] != float('Inf') else -1
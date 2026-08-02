class Solution:
    def sol(self, ind, target, coins, dp):
        if ind == 0:
            if target % coins[0] == 0:
                return 1
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        not_take = self.sol(ind - 1, target, coins, dp)

        take = 0
        if coins[ind] <= target:
            take = self.sol(ind, target - coins[ind], coins, dp)

        dp[ind][target] = take + not_take
        return dp[ind][target]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        return self.sol(n - 1, amount, coins, dp)
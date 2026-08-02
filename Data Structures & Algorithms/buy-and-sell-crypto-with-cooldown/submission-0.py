class Solution:
    def sol(self, ind, buy, n, prices, dp):
        if ind >= n:
            return 0
        
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        
        profit = 0 
        if buy:
            profit = max(-prices[ind] + self.sol(ind+1, 0, n, prices, dp), 0 + self.sol(ind+1, 1, n, prices, dp))
        else:
            profit = max(prices[ind] + self.sol(ind+2, 1, n, prices, dp), 0 + self.sol(ind+1, 0, n, prices, dp))
        
        dp[ind][buy] = profit
        return dp[ind][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]

        return self.sol(0, 1, n, prices, dp)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)

        if tot % 2 != 0:
            return False

        memo = {}

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            
            state = (i, target)
            if state in memo:
                return memo[state]

            memo[state] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[state]

        return dfs(0, tot // 2)
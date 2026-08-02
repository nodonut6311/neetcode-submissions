class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if (total_sum - target) < 0 or (total_sum - target) % 2:
            return 0

        subset_sum = (total_sum - target) // 2
        dp = {}

        def count_subsets(ind, target):
            if ind == 0:
                if target == 0 and nums[0] == 0:
                    return 2
                if target == 0 or target == nums[0]:
                    return 1
                return 0

            if (ind, target) in dp:
                return dp[(ind, target)]

            not_pick = count_subsets(ind - 1, target)

            pick = 0
            if nums[ind] <= target:
                pick = count_subsets(ind - 1, target - nums[ind])

            dp[(ind, target)] = pick + not_pick
            return dp[(ind, target)]

        return count_subsets(len(nums) - 1, subset_sum)
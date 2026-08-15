from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        res = [0] * len(nums)

        pre[0] = 1
        post[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]

        return res
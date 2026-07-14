class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = [] 

        def back(i, cur_sum):
            if cur_sum == target :
                res.append(sol[:])
                return
            if cur_sum > target or i == n:
                return 

            sol.append(nums[i])
            back(i, cur_sum + nums[i])
            sol.pop() 
            back(i+1, cur_sum)    

        back(0, 0)
        return res  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_id = {}
        n = len(nums)
        for i in range(n):
            num_id[nums[i]] = i
                        
        for j in range(n):
            compl = target - nums[j]
            if compl in num_id and j != num_id[compl]:
                return [j, num_id[compl]]
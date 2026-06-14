class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = set()
        
        for i in range(len(nums)):
            if nums[i] in temp:
                return nums[i]
            temp.add(nums[i])

        return None

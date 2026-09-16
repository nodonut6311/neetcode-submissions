class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_idx = l

        def bin(left, right):
            while left <= right:          
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        if nums[min_idx] <= target and target <= nums[-1]:   
            return bin(min_idx, len(nums)-1)
        else:
            return bin(0, min_idx - 1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        min_idx = l

        if target > nums[-1]:
            l, r = 0, min_idx - 1
        else:
            l, r = min_idx, len(nums) - 1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
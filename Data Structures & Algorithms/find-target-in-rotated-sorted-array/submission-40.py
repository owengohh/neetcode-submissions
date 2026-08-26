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


        if target == nums[min_idx]:
            return min_idx
        if min_idx == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0]:
            l, r = 0, min_idx - 1
        else:
            l, r = min_idx, len(nums) - 1
        
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1


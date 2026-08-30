class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=1
        curr_min=1
        res = nums[0]

        for i in range(len(nums)):
            tmp = curr_max
            curr_max = max(tmp * nums[i], curr_min * nums[i], nums[i])
            curr_min = min(tmp * nums[i], curr_min * nums[i], nums[i])
            res = max(res, curr_max)
        
        return res
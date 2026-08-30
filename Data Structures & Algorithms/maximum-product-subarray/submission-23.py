class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = nums[0]
        for num in nums:
            tmp = curr_max
            curr_max = max(num, tmp * num, curr_min * num)
            curr_min = min(num, tmp * num, curr_min * num)
            res = max(curr_max, res)
        return res
        
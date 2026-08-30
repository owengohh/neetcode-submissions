class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = nums[0]
        for num in nums:
            tmp = curr_max
            curr_max = max(tmp * num, curr_min * num, num)
            curr_min = min(tmp * num, curr_min * num, num)
            res = max(curr_max, res)
        return res
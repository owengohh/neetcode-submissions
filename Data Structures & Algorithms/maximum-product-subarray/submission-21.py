class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = nums[0]
        for n in nums:
            tmp = n * curr_max
            curr_max = max(tmp, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)

            res = max(curr_max, res)
        return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]


        curr_max, curr_min =  1, 1

        for n in nums:
            tmp = curr_max * n
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(tmp, curr_min * n, n)
            res = max(res, curr_max)
        
        return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        res = nums[0]
        for num in nums:
            tmp = curr_max
            curr_max = max(tmp * num, num, num * curr_min)
            curr_min = min(tmp * num, num, num * curr_min)
            
            res = max(curr_max, res)
        
        return res

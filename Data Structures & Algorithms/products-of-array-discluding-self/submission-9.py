class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre, pos = 1, 1

        for i, num in enumerate(nums):
            res[i] = pre
            pre *= num
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pos
            pos *= nums[i]


        return res
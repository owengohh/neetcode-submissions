class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pos = 1, 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= pos
            pos *= nums[i]

        return res
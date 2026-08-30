class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        pos = 1
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums)):
            left[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            right[i] = pos
            pos *= nums[i]

        res = []

        for i in range(len(nums)):
            res.append(left[i] * right[i])
        
        return res
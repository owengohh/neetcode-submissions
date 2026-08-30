class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = pos = 1
        left_sum = [0] * (len(nums))
        right_sum = [0] * (len(nums))
        for i in range(len(nums)):
            print(i)
            left_sum[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            right_sum[i] = pos
            pos *= nums[i]
        
        res = []

        for i in range(len(nums)):
            res.append(left_sum[i] * right_sum[i])
        
        return res
            
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = nums[0]

        for i in range(1, len(nums)):
            if currSub < 0:
                currSub = 0
            currSub += nums[i]
            maxSub = max(maxSub, currSub)
        
        return maxSub
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSub = 0
        maxSub = nums[0]
        for i in range(len(nums)):
            currSub += nums[i]
            maxSub = max(maxSub, currSub)
            if currSub < 0:
                currSub = 0
            
        return maxSub
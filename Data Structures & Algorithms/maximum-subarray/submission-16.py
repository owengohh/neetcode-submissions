class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSub = 0
        currMax = nums[0]

        for i in range(len(nums)):
            currSub += nums[i]
            currMax = max(currSub, currMax)
            if currSub < 0:
                currSub = 0
        
        return currMax
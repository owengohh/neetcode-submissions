class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]
        maxProduct = [nums[0]]

        for i in range(1, len(nums)):
            dp[i][0] = min(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            dp[i][1] = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            maxProduct[0] = max(maxProduct[0], dp[i][1])
        
        return maxProduct[0]

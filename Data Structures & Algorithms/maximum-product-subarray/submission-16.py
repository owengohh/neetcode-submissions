class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[float('inf'), float('-inf')] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]
        highest = [nums[0]]

        for i in range(1, len(nums)):
            dp[i][0] = min(dp[i][0], nums[i] * dp[i-1][0], nums[i] * dp[i-1][1], nums[i])
            dp[i][1] = max(dp[i][1], nums[i] * dp[i-1][0], nums[i] * dp[i-1][1], nums[i])
            highest[0] = max(highest[0], dp[i][1])
        return highest[0]

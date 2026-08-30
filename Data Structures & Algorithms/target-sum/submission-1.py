class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def dfs(i, remain):
            if i == len(nums):
                return 1 if remain == 0 else 0
            if (i, remain) in dp:
                return dp[(i, remain)]
            
            dp[(i, remain)] = dfs(i+1, remain + nums[i]) + dfs(i+1, remain - nums[i])
            return dp[(i, remain)]
        return dfs(0, target)
            
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize variables for dp[i-2] and dp[i-1]
        two_steps_back = 1 # Represents dp[i-2] for current 'i'
        one_step_back = 2  # Represents dp[i-1] for current 'i'

        # Loop from step 3 up to n
        for i in range(3, n + 1):
            current_ways = two_steps_back + one_step_back
            two_steps_back = one_step_back
            one_step_back = current_ways
        
        return one_step_back # After the loop, one_step_back will hold dp[n]
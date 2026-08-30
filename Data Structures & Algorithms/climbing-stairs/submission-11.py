class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one_step_back = 1
        two_step_back = 1

        for i in range(2, n+1):
            tmp = one_step_back
            one_step_back = one_step_back + two_step_back
            two_step_back = tmp
        
        return one_step_back
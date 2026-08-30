class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i
        return target == 0
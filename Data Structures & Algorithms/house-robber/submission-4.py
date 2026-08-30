class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        two_house_back = nums[0]
        one_house_back = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr_max = max(two_house_back + nums[i], one_house_back)
            two_house_back = one_house_back
            one_house_back = curr_max
        
        return one_house_back

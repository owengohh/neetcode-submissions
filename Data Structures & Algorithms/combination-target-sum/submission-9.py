class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def bt(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
            
            for j in range(i, len(nums)):
                if nums[j] > target - curr_sum:
                    break
                curr.append(nums[j])
                bt(j, curr, curr_sum+nums[j])
                curr.pop()
        
        bt(0, [], 0)

        return res
            
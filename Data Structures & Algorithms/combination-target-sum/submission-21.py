class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def bt(i, curr, remain):
            if remain == 0:
                res.append(curr[:])
                return

            for j in range(i, len(nums)):
                if nums[j] > remain:
                    break
                curr.append(nums[j])
                bt(j, curr, remain-nums[j])
                curr.pop()
        bt(0, [], target)
        return res
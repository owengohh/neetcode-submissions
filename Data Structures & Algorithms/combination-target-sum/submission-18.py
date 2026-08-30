class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, curr, remain):
            if remain == 0:
                res.append(curr[:])
                return
            if i > len(nums):
                return
            
            for j in range(i, len(nums)):
                num = nums[j]
                if num > remain:
                    break
                curr.append(num)
                bt(j, curr, remain-num)
                curr.pop()
        
        bt(0, [], target)
        return res


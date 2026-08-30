class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, curr, remaining):
            if remaining == 0:
                res.append(curr[:])
                return
            
            for j in range(i, len(nums)):
                num = nums[j]
                if num > remaining:
                    break
                curr.append(num)
                bt(j, curr, remaining - num)
                curr.pop()
            
        bt(0, [], target)

        return res
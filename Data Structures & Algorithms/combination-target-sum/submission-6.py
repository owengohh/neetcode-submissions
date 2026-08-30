class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(i, remaining, curr):
            if remaining == 0:
                res.append(curr.copy())
            if remaining < 0:
                return
            
            for j in range(i, len(nums)):
                num = nums[j]
                if num > remaining:
                    break
                curr.append(num)
                bt(j, remaining - num, curr)
                curr.pop()

        
        bt(0, target, [])

        return res
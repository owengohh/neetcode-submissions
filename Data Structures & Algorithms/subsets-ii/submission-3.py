class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, curr):
            if i == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            curr.append(nums[i])
            bt(i+1, curr)
            curr.pop()
            bt(i+1, curr)
        
        bt(0, [])
        return res
            
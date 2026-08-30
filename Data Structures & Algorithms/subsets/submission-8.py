class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            bt(i+1, curr)
            curr.pop()
            bt(i+1, curr)
        
        bt(0, [])
        return res
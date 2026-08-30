class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(i, curr):
            res.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                bt(j+1, curr)
                curr.pop()
        
        bt(0, [])
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(start, curr):
            res.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                bt(i+1, curr)  # Move to next index
                curr.pop()
        bt(0, [])
        return res